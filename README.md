# SI 507: Final Project

## Sanghyun Lee

[To Do List](https://github.com/shlee2112/si507final/milestones)


---

## Project Proposal
[Dropbox Paper](https://paper.dropbox.com/doc/SI507-Final-Project-by-Sanghyun-Lee-nyB9qmNUfzMIrqC4mvoIY)


## Project Description

My project will aggregate all basic information about US national parks from the [National Park Service](https://www.nps.gov/index.htm) website and will scrape 2018 visitors information from [Wikipedia](https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States). All the clean data will be automatically imported as a database. The homepage route will have a brief introduction about the site, an explanation of each route, and number of national parks store in the dataset. There will be a route where a user can see all basic information about US national parks such as a name, locations and descriptions. In another route, the user will be able to select a state to view national parks from following state. Also, users will be able to find the most popular national parks in US with a barplot of number of 2018 visitors. All the data from websites will be cached as JSON files.



## How to run

1. First, install all requirements with `pip install -r requirements.txt`
2. Second, check if there is no problem with installing mataplotlib. If there is a problem, please take a look at [here](https://github.com/shlee2112/si507final/tree/master#important-if-running-into-a-matplotlib-problem).
3. Third, open Terminal or Command Line and change to appropriate directory using `cd`
4. Fourth, use `python3 SI507project_tests.py` to run the script
5. Fifth, use `python3 SI507project_tools.py` to test the script


## How to use

1. When **SI507project_tools.py** runs, it will automatically scrape basic information about national parks from nps.gov and wikipedia. Then, it automatically clean, merge and import the data into a database called **parks.db**. When the database is fully stored, it will run Flask app.
2. When Flask app is running, copy **http://127.0.0.1:5000/** and paste on a browser url.
3. Explore different routes described on the [next section](https://github.com/shlee2112/si507final/tree/master#routes-in-this-application).


## Routes in this application
- `/` -> This is a welcome page with a brief introduction, an explanation of each route and number of national parks store in the dataset.
Screenshot:
![Screenshot of homepage](https://github.com/shlee2112/si507final/blob/master/img/home.png)

- `/info` -> This page will show all the information of national parks in United States.
Screenshot:
![Screenshot of Info page](https://github.com/shlee2112/si507final/blob/master/img/all.png)

- `/info/<statename>` -> This page will take input of a state name and will show information of national parks in a specific state.
Screenshot:
![Screenshot of Info by State page](https://github.com/shlee2112/si507final/blob/master/img/infomich.png)

- `/mostpopular` -> This page will show a barplot of park visitors in 2018 to view the most popular national park in US.
Screenshot:
![Screenshot of Most Popular page](https://github.com/shlee2112/si507final/blob/master/img/mostpop.png)

## How to run tests
When **SI507project_tools.py** runs,
1. It will check if data from nps.gov is inside **park_info.csv**.
2. It will also check if a new CSV file, **states.csv**, contains right information about states.
3. Then, it will evaluate if data from nps.gov and Wikipedia is appropriate merged as **parks.csv**.
4. Lastly, it will run `Barplot` class to check if functions are running properly and the database can produce a correct information about the most popular national park.


## In this repository:
- SI507project_tools.py
- SI507project_tests.py
- advanced_expiry_caching.py
- templates
  - index.html
  - all_nps.html
  - bystate.html
  - mostpopular.html
- cache
  - 57 cached JSON files from NPS.gov
- sample_files
  - wiki_nps.csv
  - states.csv
  - parks.db
  - parks.csv
  - park_info.csv
- img
  - mostpop.pad
  - infomich.png
  - home.png
  - database_diagram.png
  - all.png
- requirements.txt
- README.md



## Database Diagram
![Image of Database Diagram](https://github.com/shlee2112/si507final/blob/master/img/database_diagram.png)

### Description
In my database, there are **Parks** and **States** tables.

#### Parks
**Parks** table has 7 variables: 'id', 'name', 'location', 'description', 'state', 'established_date', and 'visitors_2018'. 'id' is the primary key of this table. Also, 'state' has a many-to-one relationship with 'state' of **States** table. Data from **parks.csv** is automatically imported to this table.

#### States
**States** table has 4 variables: 'id', 'state', 'abbreviation' and 'url'. 'id' is the primary key, and 'state' has a one-to-many relationship with 'state' of **Parks** table. Data from **states.csv** is automatically imported to this table.


## Requirements

To run this script, you need to install all requirements with `pip install -r requirements.txt`. You can look at my ***requirements.txt*** file to see all the applications I installed to run the script successfully.

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


## **IMPORTANT (If running into a matplotlib problem)**
***To be able to run my script using virtualenv, you may need to reinstall Python as a framework.***
***If you get a message like this:***
```
from matplotlib.backends import _macosx
RuntimeError: Python is not installed as a framework. The Mac OS X backend will not be able to function correctly if Python is not installed as a framework. See the Python documentation for more information on installing Python as a framework on Mac OS X. Please either reinstall Python as a framework, or try one of the other backends. If you are using (Ana)Conda please install python.app and replace the use of 'python' with 'pythonw'. See 'Working with Matplotlib on OSX' in the Matplotlib FAQ for more information.
```
***Please follow*** [here](https://paper.dropbox.com/doc/SI507-Final-Project-by-Sanghyun-Lee-nyB9qmNUfzMIrqC4mvoIY) ***to fix the problem, or try the following before running the virtualenv:***

```
echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
brew uninstall python3
brew install python3 --with-tcl-tk
```






---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

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
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
