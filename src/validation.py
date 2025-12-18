REQUIRED_COLUMNS = {
    "student_id",
    "course_id",
    "chapter_order",
    "time_spent",
    "score",
    "completion_status"
}

def validate_data(df):
    """
    Ensures input data meets mandatory schema.
    Prevents garbage-in-garbage-out.
    """
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if df.isnull().any().any():
        raise ValueError("Input data contains null values")

    return True
