import pandas as pd
from feature_engineering import engineer_features
from pathlib import Path
def main():
     
    while True:

        filename = input(
            "\nEnter CSV filename (or type 'exit' to quit): "
            )

        if filename.lower() == "exit":
                print("Goodbye!")
                break
        try: 
            filepath = Path("datasets") / filename
            df = pd.read_csv(filepath)
            #feature_engineering
            df = engineer_features(df)
            print(df.head())

        except FileNotFoundError as e:
            print(f"\nError: {e}")#
            continue
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            continue

if __name__ == "__main__":
    main()