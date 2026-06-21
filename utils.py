import pandas as pd
from pathlib import Path
def load_dataset(filename): 
    filepath = Path("datasets") / filename
    df = pd.read_csv(filepath)
    
    return df
def create_output_folder():
    output_folder = Path("outputs")

    if not output_folder.exists():
        output_folder.mkdir()
        
def save_dataset(df, filename):
    create_output_folder()
    new_filename = f"engineered_{filename}"
    output_path = Path("outputs") / new_filename
    df.to_csv(output_path, index=False)

    return output_path
