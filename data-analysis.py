import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    # Load the CSV data into a DataFrame
    df = pd.read_csv(file_path)

    # Clean the data
    # Replace any infinity values with NaN
    df = df.replace([np.inf, -np.inf], np.nan)

    # Drop any rows with missing values
    df = df.dropna()

    return df

def calculate_summary(df, column):
    # Calculate the mean, median, and standard deviation
    mean = df[column].mean()
    median = df[column].median()
    std_dev = df[column].std()

    return mean, median, std_dev

if __name__ == "__main__":
    file_path = 'data.csv'  # replace with your file path
    df = load_and_clean_data(file_path)

    # Assume that 'target_column' is the name of the column we are interested in
    mean, median, std_dev = calculate_summary(df, 'target_column')
    print(f'Mean: {mean}, Median: {median}, Std Dev: {std_dev}')
