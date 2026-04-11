# ---------------------------------------------------------
# Newton–Raphson Method (Pure Python, User Input: Initial Guess)
# ---------------------------------------------------------

# Step 1: Define the function and its derivative
def f(x):
    return x**2 - 2          # Example function: f(x) = x² - 2

def df(x):
    return 2*x               # Derivative: f'(x) = 2x

# Step 2: Take user input for initial guess
print("🔹 Newton–Raphson Method 🔹")
x0 = float(input("Enter initial guess (x0): "))

# Step 3: Define tolerance and maximum iterations
tolerance = 0.0001
max_iterations = 20

# Step 4: Newton–Raphson method
def newton_raphson(f, df, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        print(f"Iteration {i+1}: x = {x_new:.6f}")
        if abs(x_new - x) < tol:
            print(f"\n✅ Root found at x = {x_new:.6f} after {i+1} iterations.")
            return x_new
        x = x_new
    print("\n⚠️ Maximum iterations reached without convergence.")
    return x

# Step 5: Run method
root = newton_raphson(f, df, x0, tolerance, max_iterations)
