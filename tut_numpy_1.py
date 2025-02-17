import numpy as np

# Creating a 1D array (vector)
data = np.array([1, 2, 3, 4, 5])
print("1D Array:", data)

# Creating a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", matrix)

# Random numbers (for initializing ML model weights).
# NumPy can generate random numbers and structured data, often used for synthetic datasets.
random_data = np.random.rand(3, 3)  # 3x3 matrix with values between 0 and 1
print("Random Matrix:\n", random_data)

# Generating Normally Distributed Data (Gaussian Distribution)
normal_data = np.random.randn(1000)  # 1000 values from a normal distribution
print(normal_data[:10]) # print 1st 10 values
print("Mean:", np.mean(normal_data))
print("Standard Deviation:", np.std(normal_data))

# Matrix Multiplication
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication (used in neural networks)
result = np.dot(A, B)
print("Matrix Multiplication:\n", result)

# Inverse of a Matrix
from numpy.linalg import inv

matrix = np.array([[4, 7],
                   [2, 6]])
inverse_matrix = inv(matrix)
print("Inverse of Matrix:\n", inverse_matrix)


