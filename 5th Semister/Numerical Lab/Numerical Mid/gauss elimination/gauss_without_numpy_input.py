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

# Gauss Elimination Method in Python (without NumPy)

# Taking user input
n = int(input("Enter number of equations: "))

# Create augmented matrix (list of lists)
a = [[0 for j in range(n + 1)] for i in range(n)]
x = [0 for i in range(n)]

print("\nEnter the coefficients of each equation (including constant term):")
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input(f"a[{i+1}][{j+1}] = "))

# Forward Elimination
for i in range(n):
    if a[i][i] == 0.0:
        print("⚠️ Division by zero detected! Try rearranging equations.")
        exit()
    
    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]
        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution
x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]
    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]
    x[i] = x[i] / a[i][i]

# Display Result
print("\n✅ Solution:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.6f}")
