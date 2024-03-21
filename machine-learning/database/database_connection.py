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
    query_race_results = 'SELECT * FROM race_results'
    
    with engine.connect() as connection:
        race_df = pd.read_sql_query(sql=text(query_races), con=connection)
        race_results_df = pd.read_sql_query(sql=text(query_race_results), con=connection)

    return race_df, race_results_df

def load_new_data():
    engine = create_engine()

    query_weekly_races = 'SELECT * FROM weekly_races'
    query_race_entries = 'SELECT * FROM race_entries'

    with engine.connect() as connection:
        weekly_races_df = pd.read_sql_query(sql=text(query_weekly_races), con=connection)
        race_entries_df = pd.read_sql_query(sql=text(query_race_entries), con=connection)

    return weekly_races_df, race_entries_df
