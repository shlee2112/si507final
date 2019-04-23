# SI507project_tests.py

from SI507project_tools import *


############################################################
############################################################
####### Scrape/Clean/Save Data #######

##NPS
# scrapeNPS()


##Wikipedia
# url = 'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'
# wikiScrape(url)





# ############################################################
# ############################################################
# ####### Barplot #######

# dataset = pd.read_csv('parks.csv')
#
# nps_barplot = Barplot(dataset)
# print(nps_barplot.mostpopular())
# nps_barplot.barplot()




############################################################
############################################################
####### Import CSV to DB #######

# csv_import()





############################################################
############################################################
###### Flask #######



############################################################
#Please Comment out the top test functions/methods before running the Flask App. Otherwise, it will crash.
############################################################





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
