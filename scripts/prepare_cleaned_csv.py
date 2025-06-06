import pandas as pd
import os

# Define file paths
phishing_path = "../data/phishing_urls.csv"
legitimate_path = "../data/legitimate_urls.csv"
output_path = "../data/converted_cleaned.csv"

# Load both datasets
phishing_urls = pd.read_csv(phishing_path)
legitimate_urls = pd.read_csv(legitimate_path)

# Standardize column name
phishing_urls.columns = ["url"]
legitimate_urls.columns = ["url"]

# Add labels
phishing_urls["label"] = 1
legitimate_urls["label"] = 0

# Merge datasets
merged_df = pd.concat([phishing_urls, legitimate_urls], ignore_index=True)

# Remove duplicates and NaNs
merged_df.dropna(inplace=True)
merged_df.drop_duplicates(inplace=True)

# Save cleaned CSV
os.makedirs(os.path.dirname(output_path), exist_ok=True)
merged_df.to_csv(output_path, index=False)

print(f"✅ Created: {os.path.abspath(output_path)}")
