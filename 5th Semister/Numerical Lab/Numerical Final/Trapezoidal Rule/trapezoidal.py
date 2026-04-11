# -----------------------------------------------
# Trapezoidal Rule (Pure Python, No Libraries)
# -----------------------------------------------

# Function f(x)
def fun(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

# Single-interval trapezoidal rule on [a, b]
def trapezoidal_rule(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2.0

# Pure-Python arange: start, stop (exclusive), step
def arange(start, stop, step):
    vals = []
    x = start
    # Use a small epsilon to avoid floating rounding issues
    eps = step * 1e-12
    while x + eps < stop:
        vals.append(x)
        x += step
    return vals

# ----- Inputs fixed in code (like your example) -----
a, b = 0.0, 0.8
result = trapezoidal_rule(fun, a, b)
print(f"Trapezoidal estimate on [{a}, {b}] = {result:.6f}")

# Generate the sample array: -0.01 to 0.82 (step 0.01), stop is exclusive
array = arange(-0.01, 0.82, 0.01)

# Show a few sample values (since we aren't plotting)
print("\nSample f(x) values (every 0.1):")
for x in arange(0.0, 0.81, 0.1):
    print(f"x = {x:.1f}, f(x) = {fun(x):.6f}")

# Optional: Text-based “line” between endpoints (visual hint only)
y_a, y_b = fun(a), fun(b)
print(f"\nEndpoints: (a, f(a)) = ({a}, {y_a:.6f}), (b, f(b)) = ({b}, {y_b:.6f})")
print("Line y = f(a) + (f(b)-f(a))*(x-a)/(b-a)  (not drawn; formula shown)")
