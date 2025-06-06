import pandas as pd

# Load the dataset you used for training
df = pd.read_csv("data/converted_cleaned.csv")

# Drop the label and URL column
feature_df = df.drop(columns=["url", "status"])

# Print feature info
print(f"✅ Number of features used in training: {feature_df.shape[1]}")
print("🔍 Feature names used during training:")
for i, col in enumerate(feature_df.columns, start=1):
    print(f"{i:02d}: {col}")
