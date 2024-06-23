import pandas as pd
import numpy as np

# Generate synthetic housing data
np.random.seed(42)
n_rows = 1000

data = {
    'longitude': np.random.uniform(-124.35, -114.31, n_rows),  # Example: California longitude range
    'latitude': np.random.uniform(32.54, 41.95, n_rows),       # Example: California latitude range
    'housing_median_age': np.random.randint(1, 50, n_rows),
    'total_rooms': np.random.randint(2, 5000, n_rows),
    'total_bedrooms': np.random.randint(1, 1000, n_rows),
    'population': np.random.randint(1, 5000, n_rows),
    'households': np.random.randint(1, 1000, n_rows),
    'median_income': np.random.normal(3, 1.5, n_rows) * 1000,  # Example: Median income with normal distribution
    'median_house_value': np.random.randint(50000, 500000, n_rows)
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('generated_housing_data.csv', index=False)
