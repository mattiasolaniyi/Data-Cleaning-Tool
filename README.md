# Automated Data Cleaning Tool

## Overview

The **Automated Data Cleaning Tool** is a Python-based application designed to automate the process of cleaning raw datasets. This tool helps in handling common data issues like missing values, duplicates, and outliers. The tool outputs the cleaned data in CSV format and displays the result as an interactive HTML table.

## Data Source

The data used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets). Specifically, this project uses the **"Customer Shopping Dataset"** by Mehmet Tahir Aslan, which contains information about customers and their shopping behaviors, such as their demographic details, products bought, and spending patterns.

You can access the dataset on Kaggle here:  
[Kaggle Customer Shopping Dataset](https://www.kaggle.com/datasets/mehmettahiraslan/customer-shopping-dataset)

### **Sample Data Used for Testing**

The following sample dataset was used as the first test to evaluate the tool's functionality:

| CustomerID | Age | Gender | Product | Price | Rating |
|------------|-----|--------|---------|-------|--------|
| 1          | 25  | Male   | Shoes   | 99.99 | 4      |
| 2          | 30  | Female | Shirt   | 39.99 | 5      |
| 3          | 22  | Female | Pants   | 49.99 | 3      |
| 4          | 40  | Male   | Jacket  | 129.99| NaN    |
| 5          | 35  | Male   | Shoes   | 99.99 | 4      |
| 6          | 28  | Female | Shoes   | 109.99| 5      |

This dataset contains columns such as **Age**, **Gender**, **Product**, **Price**, and **Rating**, which may contain missing or invalid values, duplicates, or outliers.

---

## Features

- **Data Cleaning**: Automatically cleans datasets by handling missing values, removing duplicates, and detecting outliers.
- **HTML Output**: Cleaned data is displayed on a styled HTML page for easy visualization.
- **CSV Output**: Cleaned dataset is saved as `cleaned_data.csv`.
- **User-friendly**: Users just need to upload their raw dataset, and the tool does the rest.

## Technologies Used

- **Python**: The main programming language for this project.
- **Pandas**: Library for data manipulation and cleaning.
- **NumPy**: Used for handling numerical operations (e.g., filling missing values).
- **Matplotlib/Seaborn**: Visualization tools to detect outliers.
- **Bootstrap**: For styling the HTML output.
- **Web Browser**: To display the cleaned dataset in a styled HTML table.

## Requirements

Before running the project, make sure you have the following installed:

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn

You can install the required libraries with `pip`:

```bash
pip install pandas numpy matplotlib seaborn
