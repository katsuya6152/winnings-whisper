import os
from joblib import load

def load_model(output_path):
    model_path = os.path.join(output_path, "model.joblib")
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    model = load(model_path)
    return model
