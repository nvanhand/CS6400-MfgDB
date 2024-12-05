# Relational Database Setup

## Dependencies
SQLite, Python
Python libraries: sqlite3, pandas

## Project Setup
SQLite was used as the database system. Please find the installation instructions here: https://www.sqlite.org/download.html

## Data Preparation
Ensure the eos-cam.json file, clean_BuildDocumentation.xlsx, and sensors.csv files are downloaded and in the correct working directory. Using load.txt, files may be bulk loaded into the SQL database. 


    sqlite3 <db_name> < create.sql
    sqlite3 <db_name> < load.txt