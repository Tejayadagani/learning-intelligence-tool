import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads learner data from CSV.
    We keep ingestion simple and robust.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise RuntimeError(f"Failed to load data: {e}")
