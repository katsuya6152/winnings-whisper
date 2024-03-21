from sklearn import preprocessing
import pandas as pd
import datetime as dt
import numpy as np

def label_encoder(df, cols):
    return_df = df.copy()
    for col in cols:
        le = preprocessing.LabelEncoder()
        return_df[col] = return_df[col].astype(str)
        return_df[col] = pd.Series(le.fit_transform(return_df[col]))
        return_df[col] = return_df[col].replace({'nan': np.nan})
    return return_df

def clean_df(df, int_columns, float_columns, mode):
    return_df = df.copy()
    if mode == "train":
        return_df['rank'] = return_df['rank'].replace({'1': 1, '2': 1, '3': 1})
        return_df.loc[~(return_df['rank'] == 1), 'rank'] = 0

    for col in int_columns:
        return_df[col] = pd.to_numeric(return_df[col], errors='coerce').fillna(0).astype(int)
    for col in float_columns:
        return_df[col] = pd.to_numeric(return_df[col], errors='coerce')
    return return_df

def split_df(df):
    return_df = df.copy()
    train_df = return_df[return_df['date'] < dt.datetime(2021, 1,1)].drop('date', axis=1)
    val_df = return_df[(return_df['date'] >= dt.datetime(2021, 1,1)) & (return_df['date'] < dt.datetime(2022, 1,1))].drop('date', axis=1)
    test_df = return_df[return_df['date'] >= dt.datetime(2022, 1, 1)].drop('date', axis=1)
    return train_df, val_df, test_df

def split_target(df):
    X = df.drop('rank', axis=1)
    y = df['rank']
    return X, y

def preprocess_data(df, mode):
    ENCODING_COLUMNS = [
        "id", "race_name", "race_place",
        "race_state", "race_course", "race_weather",
        "sex_and_age", "sex",
        "jockey", "horse_trainer", "horse_owner"
    ]
    
    INT_COLUMNS = [
        "box", "horse_order", "horse_weight", "race_distance",
        "race_start", "age", "day_of_year", "number_of_entries",
        "difference_weight", "day_of_year"
    ]
    if mode == "train":
        INT_COLUMNS.append("rank")
    
    FLOAT_COLUMNS =[
        "burden_weight"
    ]
    
    encoded_df = label_encoder(df, ENCODING_COLUMNS)
    
    cleaned_df = clean_df(encoded_df, INT_COLUMNS, FLOAT_COLUMNS, mode)
    
    return cleaned_df
