# ---------------------------------------------------------
# Linear Regression using Stochastic Gradient Descent (SGD)
# Pure Python version with user input
# ---------------------------------------------------------

import random

print("🔹 Linear Regression using Stochastic Gradient Descent (SGD) 🔹")

# Step 1: Generate random data (y = 4 + 3x + noise)
random.seed(0)  # reproducibility
x = [2 * random.random() for _ in range(100)]
y = [4 + 3 * xi + random.gauss(0, 1) for xi in x]

# Step 2: Take user input
learning_rate = float(input("Enter learning rate (e.g., 0.01): "))
epochs = int(input("Enter number of epochs (e.g., 100): "))

# Step 3: Define SGD function
def stochastic_gradient_descent(x, y, m=0, b=0, lr=0.01, epochs=100):
    n = len(y)
    for _ in range(epochs):
        for i in range(n):
            xi = x[i]
            yi = y[i]
            y_pred = m * xi + b
            dm = -2 * xi * (yi - y_pred)
            db = -2 * (yi - y_pred)
            m -= lr * dm
            b -= lr * db
    return m, b

# Step 4: Train the model
m, b = stochastic_gradient_descent(x, y, lr=learning_rate, epochs=epochs)

# Step 5: Display results
print("\n✅ Training complete!")
print(f"Slope (m): {m:.4f}")
print(f"Intercept (b): {b:.4f}")

# Step 6: Allow user to test predictions
print("\n--- Test the Model ---")
while True:
    xi = float(input("Enter a value for x (or -1 to exit): "))
    if xi == -1:
        break
    y_pred = m * xi + b
    print(f"Predicted y = {y_pred:.3f}\n")
