import pandas as pd
import argparse

def clean_data(input_file, output_file, impute=False):
    # Read CSV
    df = pd.read_csv(input_file)

    # Drop duplicates
    df = df.drop_duplicates()

    # Handle missing values
    if impute:
        df = df.fillna(df.mean(numeric_only=True))

    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned file saved at {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output CSV file")
    parser.add_argument("--impute", action="store_true", help="Impute missing values")
    args = parser.parse_args()

    clean_data(args.input, args.output, args.impute)
