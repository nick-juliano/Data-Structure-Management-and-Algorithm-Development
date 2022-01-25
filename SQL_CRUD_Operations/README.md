# <u>Project 1</u>: SQL CRUD Operations within Python</u>

## Objectives
- Create .db file
- Create a table within the database
- Update the table with additional information
- Delete the table or information within
___
## Overview

While there are many simpler methods for storing and accessing data for use within python, SQL is a database management 
language that boasts the following benefits:

- <b>Standardization</b> - Uniformity of CRUD operations within a database
- <b>Portability</b> - Useful in a variety of circumstances and platforms
- <b>Speed</b> - Large data sets can be retrieved, revised, and filtered quickly and reliably

This makes SQL a vital component of data structure and management, and the intended storage tool for future python 
projects. 
___
## Description
The [create-db.py file](create-db.py) demonstrates use of the <i>sqlite3</i> python module to execute SQL queries 
within python code. In order, this file performs the following options:

1) Convert a [csv file](cumulative_2022.01.20_12.32.06.csv) downloaded from the [exoplanet archive](https://exoplanetarchive.ipac.caltech.edu) into a 
<i>pandas</i> dataframe
2) Iteratively generate a string of column headers with included data types
3) Reformat the data within the dataframe for compatability with SQL databases
4) Create a database file
5) Create a table within the database
6) Import the <i>pandas</i> dataframe into the database
7) (optional) delete or update the database

The created database is stored [here](db/exoplanet_archive.db)
