import numpy as np
# Simulating dataset preparation for training
np.random.seed(0)  # Ensures reproducible random numbers

# 1. Initialize random weights from a normal distribution
#weights = np.random.randn(5, 1)

weights = np.round(np.random.randn(5, 1), 2)

print("Randomly initialized weights:\n", weights)

# 2. Standardize features (Z-score normalization)
raw_data = np.array([[10, 20], [15, 25], [12, 22]])
print("Raw Data:\n", raw_data)

standardized_data = (raw_data - np.mean(raw_data, axis=0)) / np.std(raw_data, axis=0)
print("Standardized Data:\n", standardized_data)
