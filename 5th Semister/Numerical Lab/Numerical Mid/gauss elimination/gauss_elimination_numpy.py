# ---------------------------------------------------------
# Example: Solve the following system using Gauss Elimination
#
#   2x +  y -  z =  8
#  -3x -  y + 2z = -11
#  -2x +  y + 2z = -3
#
# Expected solution:
#   x = 2,  y = 3,  z = -1
# ---------------------------------------------------------

import numpy as np

# Number of equations
n = 3

# Augmented matrix (coefficients + constants)
a = np.array([
    [2, 1, -1, 8],     # Equation 1
    [-3, -1, 2, -11],  # Equation 2
    [-2, 1, 2, -3]     # Equation 3
], dtype=float)

x = np.zeros(n)

# Forward elimination
for i in range(n):
    if a[i][i] == 0.0:
        print("⚠️ Division by zero detected! Try rearranging equations.")
        break

    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]
        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back substitution
x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]
    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]
    x[i] = x[i] / a[i][i]

# Display results
print("\n✅ Solution:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.6f}")
