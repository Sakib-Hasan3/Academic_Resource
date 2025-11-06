# ---------------------------------------------------------
# Euler’s Method (Pure Python)
# Solves dy/dx = f(x, y) with given x0, y0, step size (h), and number of steps (n)
# ---------------------------------------------------------

# Step 1: Define the differential equation
def f(x, y):
    return x + y   # Example: dy/dx = x + y

# Step 2: Define initial conditions
x0 = 0.0      # initial x
y0 = 1.0      # initial y
h = 0.1       # step size
n = 10        # number of steps

# Step 3: Euler’s Method
print("🔹 Euler’s Method 🔹")
print(f"{'Step':<5}{'x':>10}{'y':>15}")

x, y = x0, y0
print(f"{0:<5}{x:>10.4f}{y:>15.6f}")

for i in range(1, n+1):
    y = y + h * f(x, y)
    x = x + h
    print(f"{i:<5}{x:>10.4f}{y:>15.6f}")

# Step 4: Final Result
print(f"\n✅ Approximate solution at x = {x:.2f} is y ≈ {y:.6f}")
