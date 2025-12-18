import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts raw learner logs into model-ready features.
    """
    features = df.groupby("student_id").agg(
        avg_time_spent=("time_spent", "mean"),
        avg_score=("score", "mean"),
        chapters_completed=("chapter_order", "count"),
        completion_status=("completion_status", "max")
    ).reset_index()

    features["chapters_completed_ratio"] = (
        features["chapters_completed"] / features["chapters_completed"].max()
    )

    return features
