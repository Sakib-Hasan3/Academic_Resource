# ---------------------------------------------------------
# Runge–Kutta 4th Order Method (Pure Python)
# Solves dy/dx = f(x, y) with y(x0) = y0
# Example: dy/dx = x + y
# ---------------------------------------------------------

# Step 1: Define the differential equation
def f(x, y):
    return x + y   # Example equation dy/dx = x + y

# Step 2: Define initial values and step size
x0 = 0.0      # initial x
y0 = 1.0      # initial y
h = 0.1       # step size
n = 10        # number of steps

# Step 3: Runge–Kutta (RK4) Method
print("🔹 Runge–Kutta (RK4) Method 🔹")
print(f"{'Step':<5}{'x':>10}{'y':>15}")

x = x0
y = y0
print(f"{0:<5}{x:>10.4f}{y:>15.6f}")

for i in range(1, n+1):
    k1 = f(x, y)
    k2 = f(x + h/2, y + (h/2)*k1)
    k3 = f(x + h/2, y + (h/2)*k2)
    k4 = f(x + h,   y + h*k3)
    y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    x = x + h
    print(f"{i:<5}{x:>10.4f}{y:>15.6f}")

# Step 4: Display final result
print(f"\n✅ Approximate solution at x = {x:.2f} is y ≈ {y:.6f}")
