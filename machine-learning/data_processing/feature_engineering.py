import re
import pandas as pd
import numpy as np

def get_race_state_features(df):
    return_df = df.copy()
    return_df["race_course"] = df["race_state"].str[1]
    return_df["race_distance"] = df["race_state"].str[2:6]
    return_df["race_weather"] = df["race_state"].str[15]
    return_df["race_state"] = df["race_state"].str[23]
    return_df["race_start"] =  df["race_state"].str[32:37].str.replace(":", "")
    return return_df

def get_sex_and_age(df):
    return_df = df.copy()
    return_df["sex"] = return_df["sex_and_age"].str[0]
    return_df["age"] = return_df["sex_and_age"].str[1]
    return return_df

def get_horse_weight(df):
    return_df = df.copy()
    return_df["difference_weight"] = return_df["horse_weight"].str[3:]
    return_df["difference_weight"] = return_df["difference_weight"].replace(re.compile("\(|\)"), "", regex=True)
    return_df[return_df['difference_weight'] == ''] = -9999
    return_df["difference_weight"] = return_df["difference_weight"].astype(int)
    return_df[return_df['difference_weight'] == -9999] = None
    return_df["horse_weight"] = return_df["horse_weight"].str[0:3]
    return return_df

def get_date(df):
    return_df = df.copy()
    return_df['date'] = return_df['date'].str.split(' ', expand=True)[0]
    return_df['date'] = pd.to_datetime(return_df['date'], format='%Y年%m月%d日')
    return_df['day_of_year'] = return_df['date'].dt.day_of_year
    return_df['date_cos'] = np.cos(2 * np.pi * return_df['day_of_year'] / return_df['day_of_year'].max())
    return_df['date_sin'] = np.sin(2 * np.pi * return_df['day_of_year'] / return_df['day_of_year'].max())
    return return_df

def get_all_feature(race_df, race_results_df):
    merge_df = pd.merge(race_df, race_results_df, on='id', how='left')
    merge_df = merge_df.dropna(subset=["id"])
    
    USE_COLUMNS = [
        "id", "race_name", "race_place", "number_of_entries", "race_state", "date",
        "rank", "box", "horse_order", "sex_and_age", "burden_weight",
        "jockey", "horse_weight", "horse_trainer", "horse_owner"
    ]
    use_df = merge_df[USE_COLUMNS]

    df = use_df.copy()
    df = get_race_state_features(df)
    df = get_sex_and_age(df)
    df = get_horse_weight(df)
    df = get_date(df)
    
    return df
