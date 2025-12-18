def preprocess(df):
    """
    Light preprocessing.
    No heavy transformations to keep explainability.
    """
    df = df.copy()
    df["time_spent"] = df["time_spent"].astype(float)
    df["score"] = df["score"].astype(float)
    return df
