import pandas as pd
import os
from urllib.parse import urlparse

# === Feature Extraction Functions ===

def get_url_length(url):
    return len(url)

def has_ip_address(url):
    import re
    # Check if the domain part contains an IP address
    ip_pattern = r'(([0-9]{1,3}\.){3}[0-9]{1,3})'
    return 1 if re.search(ip_pattern, url) else 0

def count_dots(url):
    return url.count('.')

def count_hyphens(url):
    return url.count('-')

def has_https(url):
    return 1 if urlparse(url).scheme == 'https' else 0

def get_domain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

# === Main Script ===

# Define paths
input_path = os.path.join("data", "converted_cleaned.csv")
output_path = os.path.join("data", "processed_dataset.csv")

# Load cleaned dataset
df = pd.read_csv(input_path)

# Extract features
df["url_length"] = df["url"].apply(get_url_length)
df["has_ip"] = df["url"].apply(has_ip_address)
df["dot_count"] = df["url"].apply(count_dots)
df["hyphen_count"] = df["url"].apply(count_hyphens)
df["has_https"] = df["url"].apply(has_https)

# Optionally include domain as a feature
df["domain"] = df["url"].apply(get_domain)

# Save the processed dataset
df.to_csv(output_path, index=False)

print(f"✅ Features extracted and saved to {output_path}")
