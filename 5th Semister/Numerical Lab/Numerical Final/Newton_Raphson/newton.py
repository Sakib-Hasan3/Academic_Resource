# ---------------------------------------------------------
# Newton-Raphson Method (Pure Python, No Libraries)
# ---------------------------------------------------------

# Define function and derivative
def f(x):
    return x**2 - 2

def df(x):
    return 2*x

# Newton-Raphson function
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x)/df(x)
        print(f"Iteration {i+1}: x = {x_new:.6f}")
        if abs(x_new - x) < tol:
            print(f"\n✅ Root found at x = {x_new:.6f} after {i+1} iterations.")
            return x_new
        x = x_new
    print("\n⚠️ Maximum iterations reached.")
    return x

# Inputs directly in code
x0 = 1.0  # initial guess

# Run method
root = newton_raphson(f, df, x0)
