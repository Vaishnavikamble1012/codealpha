# simple_eda.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

# Initialize settings
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 5)

# Load data
try:
    df = pd.read_csv('data.csv')
    print("Data loaded successfully!")
except FileNotFoundError:
    print("Error: data.csv file not found in current directory")
    exit()

# Basic info
print("\n=== BASIC INFO ===")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("\nFirst 5 rows:")
print(df.head())

# Data types
print("\n=== DATA TYPES ===")
print(pd.DataFrame({
    'dtype': df.dtypes,
    'missing': df.isna().sum(),
    'unique': df.nunique()
}))

# Missing values
print("\n=== MISSING VALUES ===")
msno.matrix(df)
plt.title('Missing Values')
plt.savefig('missing_values.png')
plt.close()
print("Saved missing_values.png")

# Numerical analysis
num_cols = df.select_dtypes(include=np.number).columns
if len(num_cols) > 0:
    print("\n=== NUMERICAL ANALYSIS ===")
    print(df[num_cols].describe())
    
    # Histograms
    for col in num_cols:
        df[col].hist()
        plt.title(f'Distribution of {col}')
        plt.savefig(f'{col}_histogram.png')
        plt.close()
        print(f"Saved {col}_histogram.png")

# Categorical analysis
cat_cols = df.select_dtypes(include='object').columns
if len(cat_cols) > 0:
    print("\n=== CATEGORICAL ANALYSIS ===")
    for col in cat_cols:
        print(f"\n{col} value counts:")
        print(df[col].value_counts())
        
        # Bar plots
        df[col].value_counts().plot(kind='bar')
        plt.title(f'Value Counts: {col}')
        plt.xticks(rotation=45)
        plt.savefig(f'{col}_counts.png')
        plt.close()
        print(f"Saved {col}_counts.png")

# Correlation
if len(num_cols) > 1:
    print("\n=== CORRELATION ===")
    corr = df.corr(numeric_only=True)
    print(corr)
    
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.savefig('correlation.png')
    plt.close()
    print("Saved correlation.png")

print("\nEDA completed! Check generated PNG files.")