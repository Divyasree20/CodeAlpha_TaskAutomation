import pandas as pd

# Load the dataset (Replace 'data.csv' with your actual file)
file_path = "data.csv"  # Change to your file name
df = pd.read_csv(file_path)

# ✅ 1. Remove Duplicate Rows
df = df.drop_duplicates()

# ✅ 2. Fill Missing Values
df.fillna("Unknown", inplace=True)

# ✅ 3. Convert Column Names to Lowercase
df.columns = df.columns.str.lower()

# ✅ 4. Save the cleaned data to a new file
cleaned_file_path = "cleaned_data.csv"
df.to_csv(cleaned_file_path, index=False)

print("✅ Data cleaned and saved to", cleaned_file_path)
