# SI507project_tools

import os
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from advanced_expiry_caching import Cache
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from matplotlib import pyplot as plt
import seaborn as sns



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



    ##### Scraping all parks information and save it as a CSV
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


    ## Save the merged data as a CSV file
    nps_info.to_csv('nps_info.csv', encoding='utf-8')





###### Barplot Function ######
class Popular():
    def __init__(self, data):
        self.data = data

    def barplot(self, x='name', y='visitors_2018'):
        plt.figure(figsize=(45,10))
        sns.set(font_scale=2)
        sns.barplot(x,y,data=self.data.dropna())
        plt.xticks(rotation=90)
        plt.show()

    def mostpopular(self):
        name = self.data.loc[self.data['visitors_2018'].idxmax()]['name']
        num = self.data.loc[self.data['visitors_2018'].idxmax()]['visitors_2018']
        return "{} had {} visitors in 2018".format(name, num)





#
# ###### Setting up for database ######
#
# app = Flask(__name__)
# app.debug = True
# app.use_reloader = True
# app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./parks.db'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#
# # Set up Flask debug stuff
# db = SQLAlchemy(app) # For database use
# session = db.session # to make queries easy
#
#
#
#
#
# ##### Set up Models #####
#
#
# class Parks(db.Model):
#     __tablename__ = "Parks"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     location = db.Column(db.String(64))
#     description = db.Column(db.String(64))
#     states = db.relationship('States', secondary=association, backref=db.backref('states', lazy='dynamic'), lazy='dynamic')
#     established_date = db.Column(db.String(64))
#     visitors_2018 = db.Column(db.Integer(64))
#
#
#
# class States(db.Model):
#     __tablename__ = "States"
#     id = db.Column(db.Integer, primary_key=True)
#     state = db.Column(db.String(64))
#     abbreviation = db.Column(db.String(64))
#     url = db.Column(db.String(64))
