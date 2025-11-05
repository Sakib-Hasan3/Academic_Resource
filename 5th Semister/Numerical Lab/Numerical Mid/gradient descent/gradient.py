import random

# Step 1: Generate synthetic data (y = 4 + 3x + random noise)
random.seed(0)  # reproducibility
x = [2 * random.random() for _ in range(100)]
y = [4 + 3 * xi + random.gauss(0, 1) for xi in x]  # add small noise

# Step 2: Define SGD function
def stochastic_gradient_descent(x, y, m=0, b=0, learning_rate=0.01, epochs=1000):
    n = len(y)
    for _ in range(epochs):
        for i in range(n):
            xi = x[i]
            yi = y[i]
            y_pred = m * xi + b
            dm = -2 * xi * (yi - y_pred)
            db = -2 * (yi - y_pred)
            m -= learning_rate * dm
            b -= learning_rate * db
    return m, b

# Step 3: Train model
m, b = stochastic_gradient_descent(x, y, learning_rate=0.01, epochs=100)

# Step 4: Display results
print("✅ Linear Regression using Stochastic Gradient Descent")
print(f"Slope (m): {m:.4f}")
print(f"Intercept (b): {b:.4f}")

# Step 5: Show a few predictions
print("\nSample Predictions:")
for xi in [0, 0.5, 1.0, 1.5, 2.0]:
    yi_pred = m * xi + b
    print(f"x = {xi:.1f} → Predicted y = {yi_pred:.3f}")
