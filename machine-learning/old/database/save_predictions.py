from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base

from database.database_connection import create_engine

Base = declarative_base()

def add_predict_proba_column(engine, table_name='race_entries', column_name='predict_proba'):
    Base.metadata.reflect(engine)
    table = Base.metadata.tables[table_name]
    
    if column_name not in table.c:
        with engine.connect() as conn:
            sql_statement = text(f'ALTER TABLE {table_name} ADD COLUMN {column_name} FLOAT')
            conn.execute(sql_statement)
            print(f"Added '{column_name}' column to '{table_name}' table.")
    else:
        print(f"Column '{column_name}' already exists in '{table_name}' table.")

def save_predictions(race_entries_df, predictions, table_name='race_entries', column_name='predict_proba'):
    engine = create_engine()

    add_predict_proba_column(engine, table_name, column_name)

    race_entries_df[column_name] = predictions

    race_entries_df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Saved predictions to '{table_name}' table.")