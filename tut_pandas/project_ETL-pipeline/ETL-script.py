"""
Simple Python ETL Pipeline
E = Extract data from source
T = Transform / clean data
L = Load into destination
"""

import pandas as pd
import logging
from datetime import datetime


# --------------------------------------------------
# Step 0 : Logging setup
# --------------------------------------------------

logging.basicConfig(
    filename="etl_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("ETL Pipeline Started")


# --------------------------------------------------
# Step 1 : EXTRACT
# Read data from source (CSV file)
# --------------------------------------------------

def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)

        logging.info("Data extracted successfully")
        print("Rows extracted:", len(df))

        return df

    except FileNotFoundError:
        logging.error("File not found")
        print("ERROR: Source file missing")

    except Exception as e:
        logging.error(f"Extraction error: {e}")
        print("Unexpected extraction error")


# --------------------------------------------------
# Step 2 : TRANSFORM
# Clean and process data
# --------------------------------------------------

def transform_data(df):

    # 1 Remove duplicate rows
    df = df.drop_duplicates()

    # 2 Handle missing values
    df["age"] = df["age"].fillna(df["age"].median())
    df["salary"] = df["salary"].fillna(0)

    # 3 Convert datatypes
    df["age"] = df["age"].astype(int)

    # 4 Remove invalid rows
    df = df[df["age"] > 0]  # remove negative ages

    # 5 Standardize text fields
    df["department"] = df["department"].str.lower().str.strip()

    # 6 Feature Engineering (new column)
    df["salary_after_tax"] = df["salary"] * 0.8

    # 7 Handle edge case: extremely high salary
    df.loc[df["salary"] > 1_000_000, "salary_flag"] = "High"

    logging.info("Data transformed successfully")

    return df


# --------------------------------------------------
# Step 3 : LOAD
# Save transformed data
# --------------------------------------------------

def load_data(df, output_path):

    try:

        df.to_csv(output_path, index=False)

        logging.info("Data loaded successfully")
        print("Data loaded to:", output_path)

    except Exception as e:

        logging.error(f"Loading error: {e}")
        print("Error during loading")


# --------------------------------------------------
# Step 4 : ETL PIPELINE
# Combine all steps
# --------------------------------------------------

def run_etl():

    source_file = "data_employee.csv"
    destination_file = "data_clean_employee.csv"

    # Extract
    df = extract_data(source_file)

    if df is None:
        print("Stopping pipeline")
        return

    # Transform
    df_clean = transform_data(df)

    # Load
    load_data(df_clean, destination_file)


# --------------------------------------------------
# Step 5 : Run pipeline
# --------------------------------------------------

if __name__ == "__main__":
    run_etl()
    logging.info("ETL Pipeline Finished")
