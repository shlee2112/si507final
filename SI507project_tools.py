# SI507project_tools

import os
from bs4 import BeautifulSoup
import requests
import json
import csv
import pandas as pd
from advanced_expiry_caching import Cache
from matplotlib import pyplot as plt
import seaborn as sns
from sqlalchemy import Column, Integer, Float, Date, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import io
import base64


############################################################
############################################################
###### Scraping NPS Function ######

def scrapeNPS():
    ##### CACHE

    FILENAME = "nps_cache.json"
    program_cache = Cache(FILENAME)


    url = "https://www.nps.gov" + "/index.htm"
    data = program_cache.get(url)

    if not data:
        data = requests.get(url).text
        program_cache.set(url, data, expire_in_days=1)

    soup = BeautifulSoup(data, "html.parser")


    ##### Get all state links
    state_lst = []
    for link in soup.find_all('a'):
        if '/state/' in link['href']:
            # print(link['href'])
            state_lst.append(link['href'])




    ##### Creating a new CSV called 'park_info'
    new_file = open('park_info.csv', 'w', encoding='utf8')
    new_file.write('name,type,location,description,state')
    new_file.write('\n')
    for states in state_lst:

        ##### Cache by states
        name = states.split("/")
        cache_each_state = "nps_cache_" + name[2] + ".json"
        program_cache = Cache(cache_each_state)
        url = "https://www.nps.gov" + states
        data = program_cache.get(url)

        if not data:
            data = requests.get(url).text
            program_cache.set(url, data, expire_in_days=1)
        soup = BeautifulSoup(data, "html.parser")


        ##### Scrap state's name and all parks
        state = soup.find("h1", "page-title")
        list = soup.find_all('div', {'class':'list_left'})


        for park in list:
            name = str(park.find('h3').string)
            type = str(park.find('h2').string)
            loc = str(park.find('h4').string)
            des = str(park.find('p').string)
            des = des.replace('\n', ' ')
            des = des.replace('"', "'")
            state = state.string

            row_string = '"{}","{}","{}","{}","{}"'.format(name, type, loc, des, state)
            new_file.write(row_string)
            new_file.write('\n')

    new_file.close()



    ##### Save all States info and save as a csv
    new_state_file = open('states.csv', 'w', encoding='utf8')
    new_state_file.write('state,abbreviation,url')
    new_state_file.write('\n')

    for states in state_lst:

        ##### Cache by states
        name = states.split("/")
        abbr = name[2].upper()
        url = "https://www.nps.gov" + states
        data = requests.get(url).text

        soup = BeautifulSoup(data, "html.parser")


        ##### Scrap state's name and all parks
        state = soup.find("h1", "page-title")
        list = soup.find_all('div', {'class':'list_left'})

        state_name = ""
        for park in list:
            state = state.string

        row_string = '"{}","{}","{}"'.format(state, abbr, url)
        new_state_file.write(row_string)
        new_state_file.write('\n')

    new_state_file.close()










############################################################
############################################################
###### Scraping Wikipedia Function ######

def wikiScrape(wiki_url, scrape_num = 1):
    ## Scrape data from Wikipedia
    wiki_scraped = pd.read_html(wiki_url,header=0)
    wiki_nps = wiki_scraped[scrape_num]


    ## Clean up the data
    wiki_nps.columns = ['name', 'image', 'location', 'established_date', 'area', 'visitors_2018', 'description']

    wiki_nps_cleaned = wiki_nps.drop(['image','area','location','description'], axis=1)
    wiki_nps_cleaned.name = wiki_nps_cleaned.name.str.replace('*', '')
    wiki_nps_cleaned.name = wiki_nps_cleaned.name.str.rstrip()


    ## Save as a CSV file
    wiki_nps_cleaned.to_csv('wiki_nps.csv', encoding='utf-8')


    ## Open 'park_info.csv' to merge the data together
    nps_park = pd.read_csv('park_info.csv')
    nps_info = nps_park.merge(wiki_nps_cleaned, on='name', how='left')
    nps_info = nps_info.drop(['type'], axis=1)


    ## Save the merged data as a CSV file
    nps_info.to_csv('parks.csv', encoding='utf-8')







############################################################
############################################################
###### Barplot Function ######
class Barplot():
    def __init__(self, data):
        self.data = data

    def barplot(self, x='name', y='visitors_2018'):
        img = io.BytesIO()
        plt.figure(figsize=(50,35))
        sns.set(font_scale=2)
        barplot = sns.barplot(x,y,data=self.data.dropna())
        barplot.set_title('# of National Parks Visitors in 2018')
        plt.xticks(rotation=90)
        plt.xlabel('National Parks')
        plt.ylabel('# of Visitors')
        plt.savefig(img, format='png')
        # fig = barplot.get_figure()
        # return barplot

        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        plt.close()
        # fig.savefig("nps_visitors_2018.jpg", format='png')
        # plt.show()
        return 'data:image/png;base64,{}'.format(graph_url)

    def mostpopular(self):
        name = self.data.loc[self.data['visitors_2018'].idxmax()]['name']
        num = self.data.loc[self.data['visitors_2018'].idxmax()]['visitors_2018']
        return "{} had {} visitors in 2018".format(name, num)





############################################################
############################################################
####### Scrape/Clean/Save Data #######

#NPS
scrapeNPS()


#Wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'
wikiScrape(url)





# ############################################################
# ############################################################
####### Barplot #######

# dataset = pd.read_csv('parks.csv')
# nps_barplot = Barplot(dataset)
# print(nps_barplot.mostpopular())
# nps_barplot.barplot()





###########################################################
###########################################################
##### Setup for database ######


app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./parks.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy




##### Set up Models #####

class Parks(db.Model):
    __tablename__ = "Parks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    description = db.Column(db.String(64))
    state = db.Column(db.Integer, db.ForeignKey("States.state"))
    established_date = db.Column(db.String(64))
    visitors_2018 = db.Column(db.Integer)


class States(db.Model):
    __tablename__ = "States"
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(64))
    abbreviation = db.Column(db.String(64))
    url = db.Column(db.String(64))





##### Import CSV to DB #####
# def csv_import():
Base = declarative_base()

engine = create_engine('sqlite:///./parks.db')
Base.metadata.create_all(engine)
parks_file = 'parks.csv'
parks = pd.read_csv(parks_file)
parks = parks.drop(['Unnamed: 0'], axis=1)
parks.state = parks.state.str.lower()
parks.to_sql(con=engine, index_label='id', name=Parks.__tablename__, if_exists='replace')

states_file = 'states.csv'
states = pd.read_csv(states_file)
states.state = states.state.str.lower()
states.to_sql(con=engine, index_label='id', name=States.__tablename__, if_exists='replace')








############################################################
############################################################
###### Flask #######



# Homepage
@app.route('/')
def index():
    parks = Parks.query.all()
    num_nps = len(parks)
    return render_template('index.html', num_nps=num_nps)

# All the information of national parks in US
@app.route('/info')
def info():
    all_nps = []
    parks = Parks.query.all()
    for p in parks:
        all_nps.append((p.name, p.location, p.description, p.state))
    return render_template('all_nps.html', all_parks=all_nps)


# Information of national parks in a specific state.
@app.route('/info/<statename>')
def state(statename):
    if Parks.query.filter_by(state=statename).first():
        bystate = []
        parks = Parks.query.filter_by(state=statename).all()
        for p in parks:
            bystate.append((p.name, p.location, p.description))
        return render_template('bystate.html', all_parks=bystate, state=statename.upper())
    else:
        return "There are no national park in " + statename


# Most popular national park in US in 2018.
@app.route('/mostpopular')
def popular():
    dataset = pd.read_csv('parks.csv')
    nps_barplot = Barplot(dataset)
    info = nps_barplot.mostpopular()
    img = nps_barplot.barplot()

    return render_template('mostpopular.html', info=info, nps_graph=img )



if __name__ == "__main__":
    db.create_all()
    app.run()
