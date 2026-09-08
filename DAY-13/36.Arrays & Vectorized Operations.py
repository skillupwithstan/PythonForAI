import numpy as np

# Vectorized Mean Squared Error (MSE) calculation without loops
y_true = np.array([1.0, 2.0, 3.0])
y_pred = np.array([1.1, 1.9, 3.2])

print(y_true)
print(y_pred)

mse = np.mean((y_true - y_pred) ** 2)
print("Mean Squared Error:", mse)

#mse = np.mean(np.square(y_true - y_pred))
#print("Mean Squared Error:", mse)
