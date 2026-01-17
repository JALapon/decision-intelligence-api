import pandas as pd
import io

# Function to load CSV content into a DataFrame and generate a profile
def load_csv_to_df(content):
    df = pd.read_csv(io.BytesIO(content))
    profile = {"rows": df.shape[0], "cols": df.shape[1], "columns": list(df.columns)}
    return df, profile
