# ---------------------------------------------------------
# Picard’s Method (Pure Python, No Libraries)
# Solves dy/dx = f(x, y) with y(x0) = y0
# Example: dy/dx = x + y
# ---------------------------------------------------------

# Step 1: Define the function f(x, y)
def f(x, y):
    return x + y   # Example differential equation

# Step 2: Define initial conditions and step size
x0 = 0.0      # initial x
y0 = 1.0      # initial y
h = 0.1       # step size
n = 10        # number of steps
iterations = 3  # number of Picard iterations

# Step 3: Create x values
x = [x0 + i*h for i in range(n+1)]

# Step 4: Initialize y values (start with constant y0)
y_prev = [y0 for _ in range(n+1)]

# Step 5: Perform Picard Iterations
print("🔹 Picard’s Method 🔹")
for it in range(1, iterations + 1):
    y_new = [y0]
    for i in range(1, len(x)):
        # Approximate integration using simple rectangular rule
        total = 0
        for j in range(i):
            total += h * f(x[j], y_prev[j])
        y_new.append(y0 + total)
    y_prev = y_new[:]  # update for next iteration

    # Print current iteration results
    print(f"\nIteration {it}:")
    for i in range(len(x)):
        print(f"x = {x[i]:.1f} → y ≈ {y_new[i]:.6f}")

# Step 6: Final result
print(f"\n✅ Approximate solution at x = {x[-1]:.2f} is y ≈ {y_new[-1]:.6f}")
