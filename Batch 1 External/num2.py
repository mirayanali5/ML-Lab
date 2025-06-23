import numpy as np

# 1. Create a 1-D array and display the data type
array_1d = np.array([10, 20, 30, 40, 50])
print("1-D Array:", array_1d)
print("Data type of 1-D array:", array_1d.dtype)

print("\n" + "-"*50 + "\n")

# 2. Create two 2D-arrays and perform arithmetic operations
array_2d_1 = np.array([[1, 2, 3], [4, 5, 6]])
array_2d_2 = np.array([[7, 8, 9], [10, 11, 12]])

print("First 2D Array:\n", array_2d_1)
print("Second 2D Array:\n", array_2d_2)

# Arithmetic operations
sum_array = array_2d_1 + array_2d_2
print("\nSum of two 2D arrays:\n", sum_array)

print("\n" + "-"*50 + "\n")

# 3. Concatenate along rows (axis=0)
concatenated_array = np.concatenate((array_2d_1, array_2d_2), axis=0)
print("Concatenated Array along rows:\n", concatenated_array)

print("\n" + "-"*50 + "\n")

# 4. Convert concatenated array to 1D
flattened_array = concatenated_array.flatten()
print("Flattened 1D Array:\n", flattened_array)

print("\n" + "-"*50 + "\n")

# 5. Create a 3x3 identity matrix and print details
identity_matrix = np.identity(3)
print("3x3 Identity Matrix:\n", identity_matrix)
print("Shape:", identity_matrix.shape)
print("Number of Dimensions:", identity_matrix.ndim)
print("Data type:", identity_matrix.dtype)
