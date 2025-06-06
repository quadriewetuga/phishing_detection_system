import pandas as pd
import numpy as np
import os
from tqdm import tqdm
from feature_engineering import extract_features

# File paths
data_dir = "data"
converted_path = os.path.join(data_dir, "converted_cleaned.csv")
kaggle_path = os.path.join(data_dir, "kaggle_dataset.csv")
tranco_path = os.path.join(data_dir, "tranco_dataset.csv")
output_csv_path = os.path.join(data_dir, "processed_combined.csv")
output_x_path = os.path.join(data_dir, "..", "X.npy")  # Save in project root
output_y_path = os.path.join(data_dir, "..", "y.npy")

# Load converted_cleaned
converted = pd.read_csv(converted_path)

# Load and process kaggle_dataset
kaggle = pd.read_csv(kaggle_path)
kaggle = kaggle.rename(columns={"URL": "url", "Label": "status"})
kaggle["status"] = kaggle["status"].apply(lambda x: "phishing" if x.lower() == "bad" else "legitimate")

# Load and process tranco_dataset
tranco = pd.read_csv(tranco_path, header=None, names=["rank", "domain"])
tranco["url"] = "http://" + tranco["domain"]
tranco["status"] = "legitimate"
tranco = tranco[["url", "status"]]

# Combine kaggle + tranco
combined_raw = pd.concat([kaggle[["url", "status"]], tranco], ignore_index=True)

# Extract features
print("🔍 Extracting features from kaggle + tranco data...")

features = []
labels = []

for index, row in tqdm(combined_raw.iterrows(), total=len(combined_raw), desc="Extracting features"):
    url = row['url']
    label = row['status']
    
    feat_dict = extract_features(url)
    feat_values = list(feat_dict.values())  # convert to flat list of values
    features.append(feat_values)
    labels.append(1 if label == "phishing" else 0)

# Convert to NumPy arrays (fixed!)
X = np.array(features, dtype=np.float32)
y = np.array(labels)

# Optional: Save CSV for inspection
features_df = pd.DataFrame(features, columns=extract_features("http://example.com").keys())
features_df["status"] = combined_raw["status"]
final_df = pd.concat([converted, features_df], ignore_index=True)
final_df.to_csv(output_csv_path, index=False)
print(f"✅ Combined CSV dataset saved to {output_csv_path}")

# Save features
np.save(output_x_path, X)
np.save(output_y_path, y)

print("✅ Features saved as X.npy and y.npy in project root")
print("✅ Shape of X:", X.shape)
print("✅ Number of features per sample:", X.shape[1])