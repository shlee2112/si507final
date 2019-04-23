# SI 507: Final Project

Sanghyun Lee

[To Do List](https://github.com/shlee2112/si507final/milestones)


---

## Project Proposal
[Dropbox Paper](https://paper.dropbox.com/doc/SI507-Final-Project-by-Sanghyun-Lee-nyB9qmNUfzMIrqC4mvoIY)


## Project Description

My project will aggregate all basic information about US national parks from the [National Park Service](https://www.nps.gov/index.htm) website and will scrape 2018 visitors information from [Wikipedia](https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States). The homepage route will have a brief introduction about the site, an explanation of each route, and number of national parks store in the dataset. There will be a route where a user can see all basic information about US national parks such as a name, locations and descriptions. In another route, the user will be able to select a state to view national parks from following state. Also, users will be able to find the most popular national parks in US with a bar chart of number of 2018 visitors using scraped Wikipedia data. All the data from websites will be cached as JSON files.



<!-- ## How to run

1. First, you should ... (e.g. install all requirements with `pip install -r requirements.txt`)
2. Second, you should ... (e.g. run `python programname.py runserver` or whatever else is appropriate)
3. Anything else

## How to use

1. A useful instruction goes here
2. A useful second step here
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg) -->

## Routes in this application
- `/` -> This is a welcome page with a brief introduction, an explanation of each route and number of national parks store in the dataset.
- `/info` -> This page will show all the information of national parks in United States.
- `/info/<statename>` -> This page will take input of a state name and will show information of national parks in a specific state.
- `/mostpopular` -> This page will show a barplot of park visitors in 2018 to view the most popular national park in US.


## Database Diagram
![Image of Database Diagram](https://github.com/shlee2112/si507final/blob/master/database_diagram.png)

### Description
In my database, there are **Parks**, **Cast**, and **Director**, tables.

#### Parks
**Parks** table has 7 variables: 'id', 'name', 'location', 'description', 'states', 'established_date', and 'visitors_2018'. 'id' is the primary key of this table. Also, 'states' has a many-to-one relationship with 'state' of **States** table.

#### States
**States** table has 4 variables: 'id', 'state', 'abbreviation' and 'url'. 'id' is the primary key, and 'state' has a one-to-many relationship with 'states' of **Parks** table.



## How to run tests
1. Cache and grab NPS info, then save as a csv file
2. Grab Wikipedia data and merge with NPS.csv
3. Show the most popular national park in US

## In this repository:
- SI507project_tools.py
- SI507project_tests.py
- advanced_expiry_caching.py
- templates
  - index.html
  - all_nps.html
- cache
  - 57 cache files
- nps_info.csv
- wiki_nps.csv
- park_info.csv
- database_diagram.png
- README.md


## Requirements

You need to install **BeautifulSoup** to run this script and get National Sites information. To run this script, you need to install Flask into you computer, because it needs to import Flask when the script is running. You can look at my ***requirements.txt*** file to see all the applications I install to run the script successfully.

### IMPORTANT (If running into a matplotlib problem)
***To be able to run my script using virtualenv, you may need to reinstall Python as a framework.***
***If you get a message like this:***
```
from matplotlib.backends import _macosx
RuntimeError: Python is not installed as a framework. The Mac OS X backend will not be able to function correctly if Python is not installed as a framework. See the Python documentation for more information on installing Python as a framework on Mac OS X. Please either reinstall Python as a framework, or try one of the other backends. If you are using (Ana)Conda please install python.app and replace the use of 'python' with 'pythonw'. See 'Working with Matplotlib on OSX' in the Matplotlib FAQ for more information.
```
***Please follow*** [here](https://paper.dropbox.com/doc/SI507-Final-Project-by-Sanghyun-Lee-nyB9qmNUfzMIrqC4mvoIY) ***to fix the problem, or try the following:***

```
echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
brew uninstall python3
brew install python3 --with-tcl-tk
```

#### requirement.txt
- alabaster==0.7.12
- atomicwrites==1.3.0
- attrs==19.1.0
- Babel==2.6.0
- beautifulsoup4==4.7.1
- certifi==2019.3.9
- chardet==3.0.4
- Click==7.0
- cycler==0.10.0
- dataframe==0.2.1.3
- docutils==0.14
- Flask==1.0.2
- Flask-SQLAlchemy==2.3.2
- idna==2.8
- imagesize==1.1.0
- itsdangerous==1.1.0
- Jinja2==2.10.1
- kiwisolver==1.0.1
- lxml==4.3.3
- MarkupSafe==1.1.1
- matplotlib==3.0.3
- more-itertools==7.0.0
- nose==1.3.7
- numpy==1.16.3
- packaging==19.0
- pandas==0.24.2
- pluggy==0.9.0
- py==1.8.0
- Pygments==2.3.1
- pyparsing==2.4.0
- pytest==4.4.1
- python-dateutil==2.8.0
- pytz==2019.1
- requests==2.21.0
- scipy==1.2.1
- seaborn==0.9.0
- six==1.12.0
- snowballstemmer==1.2.1
- soupsieve==1.9
- Sphinx==2.0.1
- sphinxcontrib-applehelp==1.0.1
- sphinxcontrib-devhelp==1.0.1
- sphinxcontrib-htmlhelp==1.0.2
- sphinxcontrib-jsmath==1.0.1
- sphinxcontrib-qthelp==1.0.2
- sphinxcontrib-serializinghtml==1.1.3
- SQLAlchemy==1.3.3
- tabulate==0.8.3
- urllib3==1.24.1
- Werkzeug==0.15.2


---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [ ] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [ ] Project is submitted as a Github repository
- [ ] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [ ] Includes a `requirements.txt` file containing all required modules to run program
- [ ] Includes a clear and readable README.md that follows this template
- [ ] Includes a sample .sqlite/.db file
- [ ] Includes a diagram of your database schema
- [ ] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [ ] Includes at least 3 different routes
- [ ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [ ] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [ ] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [x] Use of a new module
- [x] Use of a second new module
- [x] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [x] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [x] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [x] Caching of data you continually retrieve from the internet in some way

### Submission
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
