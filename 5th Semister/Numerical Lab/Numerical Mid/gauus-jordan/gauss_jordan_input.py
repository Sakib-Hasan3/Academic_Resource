# ---------------------------------------------------------
# Gauss–Jordan Elimination Method (Easy Version)
# Solves linear equations Ax = b using an augmented matrix [A|b]
#
# 🧮 Example Input:
# Enter number of equations: 3
#
# Equation 1:
# a[1][1] = 2
# a[1][2] = 1
# a[1][3] = -1
# a[1][4] = 8
#
# Equation 2:
# a[2][1] = -3
# a[2][2] = -1
# a[2][3] = 2
# a[2][4] = -11
#
# Equation 3:
# a[3][1] = -2
# a[3][2] = 1
# a[3][3] = 2
# a[3][4] = -3
#
# ✅ Expected Output:
# x1 = 2.000000
# x2 = 3.000000
# x3 = -1.000000
# ---------------------------------------------------------

print("🔹 Gauss–Jordan Elimination Method 🔹")

# Number of equations
n = int(input("Enter number of equations: "))

# Create augmented matrix
a = [[0.0 for j in range(n+1)] for i in range(n)]

# Take input
print("\nEnter the coefficients and constants (A|b):")
for i in range(n):
    print(f"\nEquation {i+1}:")
    for j in range(n+1):
        a[i][j] = float(input(f"a[{i+1}][{j+1}] = "))

# Gauss–Jordan Elimination
for i in range(n):
    # Make the diagonal element 1
    diag = a[i][i]
    if diag == 0:
        print("⚠️ Error: Division by zero. Try different equations.")
        exit()
    for j in range(n+1):
        a[i][j] = a[i][j] / diag

    # Make other elements in column 0
    for k in range(n):
        if k != i:
            ratio = a[k][i]
            for j in range(n+1):
                a[k][j] = a[k][j] - ratio * a[i][j]

# Print results
print("\n✅ Solution:")
for i in range(n):
    print(f"x{i+1} = {a[i][n]:.6f}")
