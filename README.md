
### My Final Project for Databases

This is my simple project that I use as a submission for my databases final project.
The requirements are as follows:
- use postgres db
- use some source data to populate the db
- use python as an interface for user to work with the db

This project is a simple data analyzer that uses sklearn, matplotlib, pandas, and numpy to work with the data and produce predictions using sklearn models, visualizations with matplotlib, and statistics through numpy. Data is handled through pd dataframes. 

## Database Source Data:

https://www.kaggle.com/datasets/guillemservera/precious-metals-data

- use this data to visualize futures data
    - visualize price trends
    - filter by type, date, range, price
- use this data to produce statistics of the data
    - average, median, volatility, rolling averages for prices
- use this data to predict 'future' futures data
    - simple linear regression
    - moving average

# frontend: 
CLI

# backend: 
python + postgres (sqlalchemy)

## how to run

# setup your postgres DB on localhost.

- adjust src.back.models.py appropriately 
    - I have a schema for the tables defined in each table's table_args
    - I also set the connection params which you may have to change, consider using a .env if you care about security

# setup python environment (use the venv)
- source venv/bin/activate
- pip install -r requirements.txt

# load the database 

- copy the models.py structures into the load_db.ipynb notebook accordingly
- adjust the connection parameters too
- run through the script to put the csvs into the db

# run the CLI
- python3 main.py