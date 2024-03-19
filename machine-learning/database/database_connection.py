import os
import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy import text
import pandas as pd

load_dotenv(dotenv_path='../.env')

def get_database_url():
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASS')
    host = os.environ.get('HOST')
    port = os.environ.get('DB_PORT')
    database = os.environ.get('DB_NAME')
    return f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'

def create_engine():
    url = get_database_url()
    engine = sqlalchemy.create_engine(url)
    return engine

def load_data():
    engine = create_engine()

    query_races = 'SELECT * FROM races'
    race_df = pd.read_sql_query(sql=text(query_races), con=engine.connect())

    query_race_results = 'SELECT * FROM race_results'
    race_results_df = pd.read_sql_query(sql=text(query_race_results), con=engine.connect())

    return race_df, race_results_df
