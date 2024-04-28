from sklearn import preprocessing
import pandas as pd
import datetime as dt
import numpy as np
from joblib import dump, load

def label_encoder(df, cols, mode, output_path):
    return_df = df.copy()
    return_df[cols] = return_df[cols].fillna('missing')

    oe = preprocessing.OrdinalEncoder(
        handle_unknown="use_encoded_value",
        unknown_value=-1,
    )

    if mode == "train":
        return_df[cols] = oe.fit_transform(return_df[cols])
        dump(oe, f'{output_path}/categories.joblib')
    elif mode == "predict":
        loaded_encoder = load(f'{output_path}/categories.joblib')
        return_df[cols] = loaded_encoder.transform(return_df[cols])
    else:
        raise ValueError("Unsupported mode. Use 'train' or 'predict'.")
    return_df = return_df.replace({'nan': np.nan})
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

def preprocess_data(df, mode, output_path):
    ENCODING_COLUMNS = [
        "race_name", "race_place",
        "race_state", "race_course", "race_weather",
        "sex_and_age", "sex",
        "jockey", "horse_trainer", "horse_owner"
    ]
    
    INT_COLUMNS = [
        "id", "box", "horse_order", "horse_weight", "race_distance",
        "race_start", "age", "day_of_year", "number_of_entries",
        "difference_weight", "day_of_year"
    ]
    if mode == "train":
        INT_COLUMNS.append("rank")
    
    FLOAT_COLUMNS =[
        "burden_weight"
    ]
    
    encoded_df = label_encoder(df, ENCODING_COLUMNS, mode, output_path)
    
    cleaned_df = clean_df(encoded_df, INT_COLUMNS, FLOAT_COLUMNS, mode)
    
    return cleaned_df
