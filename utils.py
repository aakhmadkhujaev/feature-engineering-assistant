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

def select_target_column(df):
    columns = df.columns

    for index, column in enumerate(columns, start=1):
        print("\nAvailable Columns:")
        print(f"{index}. {column}")
    while True:
        try:
            target_choice = int(input("Enter target column number: "))

            if 1 <= target_choice <= len(columns):
                target_column = columns[target_choice - 1]
                return target_column

            print("Invalid column number. Please try again.")

        except ValueError:
            print("Please enter a valid number.")


