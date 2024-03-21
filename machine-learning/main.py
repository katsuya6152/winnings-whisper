import os
import argparse
from database.database_connection import load_data, load_new_data
from data_processing.feature_engineering import get_all_feature
from data_processing.preprocessing import preprocess_data, split_df, split_target
from models.model_training import train_and_evaluate_model
from evaluations.evaluate_model import evaluate_model_performance
from database.model_evaluation import save_evaluation
from models.load_model import load_model
from database.save_predictions import save_predictions

def train(mode, model_version, output_path):
    print(f"Running training mode with model version: {model_version}")

    race_df, race_results_df = load_data()
    feature_engineered_df = get_all_feature(race_df, race_results_df, mode)
    preprocessed_df = preprocess_data(feature_engineered_df, mode)
    train_df, val_df, test_df = split_df(preprocessed_df)

    X_train, y_train = split_target(train_df)
    X_val, y_val = split_target(val_df)
    X_test, y_test = split_target(test_df)

    model, evaluation_results = train_and_evaluate_model(X_train, y_train, X_val, y_val, output_path)
    evaluation_results = evaluate_model_performance(model, X_test, y_test, model_version, output_path)

    save_evaluation(evaluation_results)

def predict(mode, model_version, output_path):
    print(f"Running prediction mode with model version: {model_version}")

    weekly_races_df, race_entries_df = load_new_data()
    feature_engineered_df = get_all_feature(weekly_races_df, race_entries_df, mode)
    preprocessed_df = preprocess_data(feature_engineered_df, mode).drop('date', axis=1)

    model = load_model(output_path)
    predictions = model.predict_proba(preprocessed_df)[:, 1]

    save_predictions(race_entries_df, predictions)

def main(mode, model_version):
    output_path = f"output/{model_version}"
    os.makedirs(os.path.join(output_path), exist_ok=True)

    if mode == 'train':
        train(mode, model_version, output_path)
    elif mode == 'predict':
        predict(mode, model_version, output_path)
    else:
        raise ValueError("Unsupported mode. Use 'train' or 'predict'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train and evaluate a model or make predictions with specified version.')
    parser.add_argument('mode', choices=['train', 'predict'], help="Mode to run the script in: 'train' or 'predict'.")
    parser.add_argument('model_version', type=str, help='The version of the model to train, evaluate, or use for predictions.')
    
    args = parser.parse_args()
    
    main(args.mode, args.model_version)
