# SI507project_tests.py

from SI507project_tools import *
from flask import Flask


####### Scrape/Clean/Save Data #######

scrapeNPS()

url = 'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'
wikiScrape(url)



####### Barplot #######

dataset = pd.read_csv('nps_info.csv')

nps_barplot = Popular(dataset)
print(nps_barplot.mostpopular())




####### Flask #######

#
# # Homepage
# @app.route('/')
# def index():
#     nps = Parks.query.all()
#     num_nps = len(nps)
#     return render_template('index.html', num_nps=num_nps)
#     return
#
# # All the information of national parks in US
# @app.route('/info')
# def info():
#
#     return
#
# # Information of national parks in a specific state.
# @app.route('/info/<statename>')
# def state(state):
#
#     return
#
# # Most popular national park in US in 2018.
# @app.route('/mostpopular')
# def popular():
#     dataset = pd.read_csv('nps_info.csv')
#     nps_barplot = Popular(dataset)
#     info = nps_barplot.mostpopular()
#     return info
#
#
# if __name__ == "__main__":
#     db.create_all()
#     app.run()
