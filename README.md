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
- `/mostpopular` -> This page will show a bar chart of park visitors in 2018 to view the most popular national park in US.


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

#### requirement.txt

***To be provided***

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
