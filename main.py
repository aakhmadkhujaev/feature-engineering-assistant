import pandas as pd
from feature_engineering import engineer_features
from utils import load_dataset, save_dataset, create_output_folder, select_target_column
from report import generate_report

def main():
     
    while True:

        filename = input(
            "\nEnter CSV filename (or type 'exit' to quit): "
            )

        if filename.lower() == "exit":
                print("Goodbye!")
                break
        try:
            df = load_dataset(filename)
            target_column = select_target_column(df)
            print(target_column)
            original_columns = df.shape[1]

            df = engineer_features(df, target_column)
            final_columns = df.shape[1]
            
            output_path = save_dataset(df, filename)
            
            
            generate_report(
                original_columns,
                final_columns,
                output_path
            )
            
            print("\n✓ Feature engineering completed!")
            print(f"\nDataset saved to: {output_path}")

        except FileNotFoundError as e:
            print(f"\nError: {e}")#
            continue
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            continue

if __name__ == "__main__":
    main()