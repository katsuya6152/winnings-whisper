import argparse
from database.database_connection import load_data
from data_processing.feature_engineering import get_all_feature
from data_processing.preprocessing import preprocess_data, split_df, split_target
from models.model_training import train_and_evaluate_model
from evaluations.evaluate_model import evaluate_model_performance
from database.model_evaluation import save_evaluation

def main(model_version):
    race_df, race_results_df = load_data()

    feature_engineered_df = get_all_feature(race_df, race_results_df)

    preprocessed_df = preprocess_data(feature_engineered_df)

    train_df, val_df, test_df = split_df(preprocessed_df)

    X_train, y_train = split_target(train_df)
    X_val, y_val = split_target(val_df)
    X_test, y_test = split_target(test_df)

    model, evaluation_results = train_and_evaluate_model(X_train, y_train, X_val, y_val)

    evaluation_results = evaluate_model_performance(model, X_test, y_test, model_version)

    save_evaluation(evaluation_results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train and evaluate a model with specified version.')
    parser.add_argument('model_version', type=str, help='The version of the model to train and evaluate.')
    
    args = parser.parse_args()
    
    main(args.model_version)
