# Relational Database Setup

## Dependencies
SQLite, Python
Python libraries: sqlite3, pandas

## Project Setup
SQLite was used as the database system. Please find the installation instructions here: https://www.sqlite.org/download.html

## Data Preparation
Ensure the eos-cam.json file, clean_BuildDocumentation.xlsx, and sensors.csv files are downloaded and in the correct working directory. Run the following from the **repo root**: 

    sqlite3 mfgdb < 1_relational_db/create.sql
    sqlite3 mfgdb < 1_relational_db/load.txt

After the database is initialized and lodaed, the load_daq.py function can be ran as:

    python3 1_relational_db/load_daq.py

## Analysis

Some example queries can be found 