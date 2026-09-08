import numpy as np

# Convert standard Python list to an array
arr = np.array([1, 2, 3, 4, 5])
print("Array from list:", arr)
print("Index of maximum value:", np.argmax(arr))

# Generate pre-filled or ranged arrays
zeros = np.zeros((3, 3))       # 3x3 matrix containing only zeros
ones = np.ones((2, 4))         # 2x4 matrix containing only ones
ranged = np.arange(0, 10, 2)   # Array from 0 to 8, stepping by 2

print("Zeros array:\n", zeros)
print("Ones array:\n", ones)
print("Ranged array:", ranged)