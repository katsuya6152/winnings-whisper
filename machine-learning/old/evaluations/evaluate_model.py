import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve
import pandas as pd
import lightgbm as lgbm

def evaluate_model_performance(model, X_test, y_test, version, output_dir):
    y_pred = model.predict_proba(X_test)[:, 1]
    y_pred_binary = model.predict(X_test)
    
    auc_score = roc_auc_score(y_test, y_pred)
    print(f'Test AUC Score: {auc_score}')
    
    cm = confusion_matrix(y_test, y_pred_binary)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig(f"{output_dir}/confusion_matrix.png")
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
    plt.savefig(f"{output_dir}/roc_curve.png")
    plt.close()

    feature_importances = pd.DataFrame(model.feature_importances_,
                                        index = X_test.columns,
                                        columns=['importance']).sort_values('importance', ascending=False)
    print(feature_importances)

    lgbm.plot_importance(model, importance_type='split', max_num_features=10)
    plt.title('Feature Importance')
    plt.savefig(f"{output_dir}/feature_importance.png")
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
