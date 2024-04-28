import datetime as dt
import json
import os
import re

import lightgbm as lgbm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
from joblib import dump
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve

from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, Float, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import JSON

def handler(event, context):
    load_dotenv()
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASS')
    host = os.environ.get('DB_HOST')
    port = os.environ.get('DB_PORT')
    database = os.environ.get('DB_NAME')
    url = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'

    engine = create_engine(url)

    query_races = 'SELECT * FROM races'
    query_race_results = 'SELECT * FROM race_results'
    
    with engine.connect() as connection:
        race_df = pd.read_sql_query(sql=text(query_races), con=connection)
        race_results_df = pd.read_sql_query(sql=text(query_race_results), con=connection)

    USE_COLUMNS = [
        "id", "race_name", "race_place", "number_of_entries", "race_state", "date",
        "box", "horse_order", "sex_and_age", "burden_weight",
        "jockey", "horse_weight", "horse_trainer", "horse_owner"
    ]

    merge_df = pd.merge(race_df, race_results_df, on='id', how='left').dropna(subset=["id"])
    USE_COLUMNS.append("rank")
    use_df = merge_df[USE_COLUMNS]

    df = use_df.copy()
    df = get_race_state_features(df)
    df = get_sex_and_age(df)
    df = get_horse_weight(df)
    df = get_date(df)

    ENCODING_COLUMNS = [
        "race_name", "race_place",
        "race_state", "race_course", "race_weather",
        "sex_and_age", "sex",
        "jockey", "horse_trainer", "horse_owner"
    ]
    
    INT_COLUMNS = [
        "id", "box", "horse_order", "horse_weight", "race_distance",
        "race_start", "age", "day_of_year", "number_of_entries",
        "difference_weight", "day_of_year", "rank"
    ]
    
    FLOAT_COLUMNS =[
        "burden_weight"
    ]
    
    encoded_df = label_encoder(df, ENCODING_COLUMNS)
    cleaned_df = clean_df(encoded_df, INT_COLUMNS, FLOAT_COLUMNS)

    train_df, val_df, test_df = split_df(cleaned_df)

    X_train, y_train = split_target(train_df)
    X_val, y_val = split_target(val_df)
    X_test, y_test = split_target(test_df)

    model = train_and_evaluate_model(X_train, y_train, X_val, y_val)
    evaluation_results = evaluate_model_performance(model, X_test, y_test, "v0.0")

    save_evaluation(evaluation_results, engine)

    return


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

def label_encoder(df, cols):
    return_df = df.copy()
    return_df[cols] = return_df[cols].fillna('missing')

    oe = preprocessing.OrdinalEncoder(
        handle_unknown="use_encoded_value",
        unknown_value=-1,
    )

    return_df[cols] = oe.fit_transform(return_df[cols])
    dump(oe, f'./categories.joblib')
    return_df = return_df.replace({'nan': np.nan})
    return return_df

def clean_df(df, int_columns, float_columns):
    return_df = df.copy()
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

def train_and_evaluate_model(X_train, y_train, X_val, y_val):
    params = {
        "objective": "binary",
        "metric": "auc",
        "boosting_type": "gbdt",
        "n_estimators": 10000,
        "random_state": 42,
    }

    clf = lgbm.LGBMClassifier(**params)

    clf.fit(
        X_train,
        y_train,
        eval_set=[(X_train, y_train), (X_val, y_val)],
        eval_metric="auc",
        callbacks=[
            lgbm.early_stopping(stopping_rounds=100, verbose=True), 
            lgbm.log_evaluation(10)
        ]
    )

    y_pred_val = clf.predict_proba(X_val)[:, 1]
    val_auc = roc_auc_score(y_val, y_pred_val)

    print(f"Validation AUC: {val_auc}")

    model_filename = os.path.join("./model.joblib")
    dump(clf, model_filename)

    return clf

def evaluate_model_performance(model, X_test, y_test, version):
    y_pred = model.predict_proba(X_test)[:, 1]
    y_pred_binary = model.predict(X_test)
    
    auc_score = roc_auc_score(y_test, y_pred)
    print(f'Test AUC Score: {auc_score}')
    
    cm = confusion_matrix(y_test, y_pred_binary)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig(f"./confusion_matrix.png")
    plt.close()

    fpr, tpr, _ = roc_curve(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % auc_score)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.savefig(f"./roc_curve.png")
    plt.close()

    feature_importances = pd.DataFrame(model.feature_importances_,
                                        index = X_test.columns,
                                        columns=['importance']).sort_values('importance', ascending=False)
    print(feature_importances)

    lgbm.plot_importance(model, importance_type='split', max_num_features=10)
    plt.title('Feature Importance')
    plt.savefig(f"./feature_importance.png")
    plt.close()

    evaluation_results = {
        'importances': feature_importances, 
        'AUC': auc_score,
        'TP': int(cm[1][1]),
        'FP': int(cm[0][1]),
        'FN': int(cm[1][0]),
        'TN': int(cm[0][0]),
        'FPR': fpr, 
        'TPR': tpr,
        'memo': 'memo',
        'version': version,
    }

    return evaluation_results

Base = declarative_base()

class ModelEvaluation(Base):
    __tablename__ = 'model_evaluation'
    
    id = Column(Integer, primary_key=True)
    feature_importance_json = Column(JSON)
    TP = Column(Integer)
    FP = Column(Integer)
    FN = Column(Integer)
    TN = Column(Integer)
    FPR = Column(JSON)
    TPR = Column(JSON)
    AUC = Column(Float)
    memo = Column(Text)
    version = Column(String(255))
    created_date = Column(DateTime, default=dt.datetime.utcnow)

def save_evaluation(evaluation_results, engine):
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    new_evaluation = ModelEvaluation(
        feature_importance_json=evaluation_results["importances"].to_json(),
        TP=evaluation_results["TP"],
        FP=evaluation_results["FP"],
        FN=evaluation_results["FN"],
        TN=evaluation_results["TN"],
        FPR=json.dumps(evaluation_results["FPR"].tolist()),
        TPR=json.dumps(evaluation_results["TPR"].tolist()),
        AUC=evaluation_results["AUC"],
        memo=evaluation_results["memo"],
        version=evaluation_results["version"],
        created_date=dt.datetime.utcnow()
    )
    
    session.add(new_evaluation)
    session.commit()
    session.close()