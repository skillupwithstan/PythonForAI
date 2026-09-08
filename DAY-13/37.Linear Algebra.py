import numpy as np
# Forward pass of a simple neural network layer
X = np.array([[0.5, 1.2]])      # 1x2 input batch
W = np.array([[0.2, 0.8],      # 2x2 weight matrix
              [0.4, 0.1]])
b = np.array([0.1, 0.2])        # Bias

# Matrix multiplication + bias addition
layer_output = np.dot(X, W) + b
#layer_output = X @ W + b
print("Layer output:", layer_output)
