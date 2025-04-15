import pandas as pd

def load_dataset(filepath):
    df = pd.read_csv(filepath)
    print("Dataset loaded successfully.")
    return df
