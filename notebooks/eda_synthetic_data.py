import pandas as pd

# Load the dataset
df = pd.read_table('../data/in/synthetic_protein_interactions.tsv', sep='\t')

# Show the first few rows
print("\n---- First 10 rows in the dataset")
print(df.head(10))

# List the columns in the dataset
print("\n---- Columns in the dataset")
for column in df.columns:
    print(f"\t{column}")

# Get basic info about the datasets
print("\n---- Summary Dataframe")
print(df.info())

# Check for missing values
print("\n---- Check missing values")
print(df.isnull().sum())

# Show summary statistics for numeric columns
print("\n---- Describe Dataframe statistics")
print(df.describe())

# Count the unique number of proteins in each column
print("\n---- Number of unique proteins per column.")
print('Unique proteins in column protein_a:', df['source'].nunique())
print('Unique proteins in column protein_b:', df['target'].nunique())