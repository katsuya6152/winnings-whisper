import lightgbm as lgbm
from sklearn.metrics import roc_auc_score, confusion_matrix
import numpy as np

def train_and_evaluate_model(X_train, y_train, X_val, y_val):

    # train_set = lgbm.Dataset(X_train, y_train)
    # val_set = lgbm.Dataset(X_val, y_val)

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

    return clf, {"val_auc": val_auc}

def calculate_model_metrics(model, X_test, y_test):

    y_pred_test = model.predict_proba(X_test)[:, 1]
    test_auc = roc_auc_score(y_test, y_pred_test)

    y_pred_binary = np.where(y_pred_test > 0.5, 1, 0)
    cm = confusion_matrix(y_test, y_pred_binary)

    print(f"Test AUC: {test_auc}")
    print("Confusion Matrix:")
    print(cm)

    return {"test_auc": test_auc, "confusion_matrix": cm}
