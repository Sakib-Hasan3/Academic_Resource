# ---------------------------------------------------------
# Milne’s Predictor–Corrector Method (Pure Python)
# Example: dy/dx = x + y, with y(0) = 1
# ---------------------------------------------------------

# Step 1: Define the differential equation
def f(x, y):
    return x + y   # Example ODE

# Step 2: Define initial values and step size
x0 = 0.0
y0 = 1.0
h = 0.1
n = 10  # number of steps to compute

# Step 3: Use Runge–Kutta (RK4) for the first 3 points (Milne needs 4)
def rk4(f, x0, y0, h):
    k1 = f(x0, y0)
    k2 = f(x0 + h/2, y0 + (h/2)*k1)
    k3 = f(x0 + h/2, y0 + (h/2)*k2)
    k4 = f(x0 + h, y0 + h*k3)
    return y0 + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

# Step 4: Generate first 4 points using RK4
x = [x0]
y = [y0]
for i in range(3):
    y_next = rk4(f, x[i], y[i], h)
    x.append(x[i] + h)
    y.append(y_next)

# Step 5: Milne’s Predictor–Corrector loop
print("🔹 Milne’s Predictor–Corrector Method 🔹")
print(f"{'Step':<5}{'x':>10}{'y':>15}")

for i in range(len(x)):
    print(f"{i:<5}{x[i]:>10.4f}{y[i]:>15.6f}")

for i in range(3, n):
    # Predictor formula
    y_pred = y[i-3] + (4*h/3)*(2*f(x[i], y[i]) - f(x[i-1], y[i-1]) + 2*f(x[i-2], y[i-2]))
    x_next = x[i] + h

    # Corrector formula (one iteration)
    y_corr = y[i-1] + (h/3)*(f(x_next, y_pred) + 4*f(x[i], y[i]) + f(x[i-1], y[i-1]))

    # Append corrected value
    x.append(x_next)
    y.append(y_corr)

    print(f"{i+1:<5}{x_next:>10.4f}{y_corr:>15.6f}")

# Step 6: Display final result
print(f"\n✅ Approximate solution at x = {x[-1]:.2f} is y ≈ {y[-1]:.6f}")
