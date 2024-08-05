import numpy as np
import matplotlib.pyplot as plt

# Set the size of the matrix (n rows and m columns)
n, m = 10, 5  # Example: 10 rows and 5 columns

# Create a random matrix with values between 0 and 1
A = np.random.rand(n, m)

for i in A: print(i)


# Create a figure for plotting
plt.figure(figsize=(10, 6))

# Plot each column of the matrix
for i in range(A.shape[1]):
    plt.plot(A[:, i], label=f'Column {i+1}')

# Add labels and title
plt.xlabel('Row Index')
plt.ylabel('Value')
plt.title('Plot of Each Column in the Matrix')

# Add a legend to the plot
plt.legend()

# Add a grid for better readability
plt.grid(True)

# Display the plot
plt.show()
