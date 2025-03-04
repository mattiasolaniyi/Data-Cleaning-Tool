import pandas as pd
import numpy as np

# Create sample data with common data issues
data = {
    "ID": [1, 2, 3, 4, 5, 5],  # Duplicate ID
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Eve"],  # Duplicate Name
    "Age": [25, np.nan, 35, 200, 29, 29],  # Contains missing value & outlier (200)
    "Salary": [50000, 60000, np.nan, 80000, 70000, 70000],  # Missing value & duplicate
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"]  # Duplicates in Department
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("sample_data.csv", index=False)

# Display dataset summary
print("Sample Data:")
print(df)
print("\nData Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for duplicates
print("\nDuplicate Rows:")
print(df[df.duplicated()])

# Check for outliers (example: age above 100)
print("\nPotential Outliers in Age:")
print(df[df["Age"] > 100])

print("\nSample data created and saved as 'sample_data.csv' successfully!")
