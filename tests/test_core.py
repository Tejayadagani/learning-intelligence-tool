import pandas as pd
from src.validation import validate_data
from src.features import build_features

def test_validation_passes():
    df = pd.DataFrame({
        "student_id": [1],
        "course_id": [101],
        "chapter_order": [1],
        "time_spent": [30],
        "score": [80],
        "completion_status": [1]
    })
    assert validate_data(df) is True

def test_feature_generation():
    df = pd.DataFrame({
        "student_id": [1, 1],
        "course_id": [101, 101],
        "chapter_order": [1, 2],
        "time_spent": [30, 40],
        "score": [80, 90],
        "completion_status": [1, 1]
    })
    features = build_features(df)
    assert "avg_score" in features.columns
    assert features.shape[0] == 1
