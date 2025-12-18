import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from ingestion import load_data
from validation import validate_data
from preprocessing import preprocess
from features import build_features

MODEL_DIR = "models/"

def train_models():
    df = load_data("data/sample_input.csv")
    validate_data(df)
    df = preprocess(df)

    features = build_features(df)

    X = features[[
        "avg_time_spent",
        "avg_score",
        "chapters_completed_ratio"
    ]]
    y = features["completion_status"]

    # Course Completion Model
    completion_model = LogisticRegression(random_state=42)
    completion_model.fit(X, y)

    # Dropout Risk Model
    dropout_model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    dropout_model.fit(X, y)

    joblib.dump(completion_model, MODEL_DIR + "completion_model.pkl")
    joblib.dump(dropout_model, MODEL_DIR + "dropout_model.pkl")

    print("Models trained and saved successfully.")

if __name__ == "__main__":
    train_models()
