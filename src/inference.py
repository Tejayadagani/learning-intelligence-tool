import joblib
from ingestion import load_data
from validation import validate_data
from preprocessing import preprocess
from features import build_features

MODEL_PATH_COMPLETION = "models/completion_model.pkl"
MODEL_PATH_DROPOUT = "models/dropout_model.pkl"

def run_inference(input_path: str):
    """
    Loads data, runs preprocessing, builds features,
    loads trained models, and generates predictions.
    """

    # Load & validate input
    df = load_data(input_path)
    validate_data(df)
    df = preprocess(df)

    # Feature engineering
    features = build_features(df)

    X = features[
        ["avg_time_spent", "avg_score", "chapters_completed_ratio"]
    ]

    # Load models
    completion_model = joblib.load(MODEL_PATH_COMPLETION)
    dropout_model = joblib.load(MODEL_PATH_DROPOUT)

    # Predictions
    features["completion_prediction"] = completion_model.predict(X)
    features["dropout_risk"] = dropout_model.predict(X)

    return df, features
