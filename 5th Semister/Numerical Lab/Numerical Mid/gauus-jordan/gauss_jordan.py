# ---------------------------------------------------------
# Gauss–Jordan Elimination Method (Fixed Input Example)
# Solves linear equations Ax = b using an augmented matrix [A|b]
#
# Example system:
#   2x +  y -  z =  8
#  -3x -  y + 2z = -11
#  -2x +  y + 2z =  -3
#
# Expected Solution:
#   x = 2,  y = 3,  z = -1
# ---------------------------------------------------------

print("🔹 Gauss–Jordan Elimination Method (Fixed Example) 🔹")

# Number of equations
n = 3

# Augmented matrix [A|b]
a = [
    [2, 1, -1, 8],     # Equation 1
    [-3, -1, 2, -11],  # Equation 2
    [-2, 1, 2, -3]     # Equation 3
]

# Gauss–Jordan Elimination
for i in range(n):
    # Make the diagonal element 1
    diag = a[i][i]
    if diag == 0:
        print("⚠️ Error: Division by zero. Try different equations.")
        exit()
    for j in range(n + 1):
        a[i][j] = a[i][j] / diag

    # Make all other elements in the column zero
    for k in range(n):
        if k != i:
            ratio = a[k][i]
            for j in range(n + 1):
                a[k][j] = a[k][j] - ratio * a[i][j]

# Print results
print("\n✅ Solution:")
for i in range(n):
    print(f"x{i+1} = {a[i][n]:.6f}")
