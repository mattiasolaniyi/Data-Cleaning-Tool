import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV File
file_path = input("Enter the path of the CSV file: ")
df = pd.read_csv(file_path)

print("\n📋 Raw Data Preview:")
print(df.head())

# Show basic info
print("\n📊 Dataset Summary:")
print(df.describe())

# Check for missing values
print("\n❌ Missing Values:")
print(df.isnull().sum())

# Fill missing values (Numeric: Median, Categorical: Mode)
for col in df.select_dtypes(include=np.number).columns:
    df[col].fillna(df[col].median(), inplace=True)
for col in df.select_dtypes(exclude=np.number).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Identify Outliers using IQR
numerical_cols = df.select_dtypes(include=np.number).columns
Q1 = df[numerical_cols].quantile(0.25)
Q3 = df[numerical_cols].quantile(0.75)
IQR = Q3 - Q1
outliers = (df[numerical_cols] < (Q1 - 1.5 * IQR)) | (df[numerical_cols] > (Q3 + 1.5 * IQR))
outlier_rows = df[outliers.any(axis=1)]

print("\n⚠️ Outliers Detected:")
print(outlier_rows)

# Save Cleaned Data
cleaned_file_path = "cleaned_data.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"\n✅ Cleaned data saved as: {cleaned_file_path}")

# Visualization - Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[numerical_cols])
plt.title("Boxplot of Cleaned Data (Outliers Highlighted)")
plt.savefig("boxplot.png")
plt.show()
