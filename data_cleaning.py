import pandas as pd
import numpy as np

def clean_nulls(df):
    df.fillna(method='ffill', inplace=True)  # Forward fill for missing values
    df.dropna(inplace=True)  # Drop rows with any NaN values
    return df

def remove_duplicates(df):
    df.drop_duplicates(inplace=True)  # Drop duplicate rows
    return df

def handle_outliers(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
    return df

if __name__ == '__main__':
    # Example usage
    df = pd.read_csv('your_raw_data.csv')
    df = clean_nulls(df)
    df = remove_duplicates(df)
    df = handle_outliers(df)
    df.to_csv('cleaned_data.csv', index=False)
