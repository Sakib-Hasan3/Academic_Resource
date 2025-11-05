# ---------------------------------------------------------
# Logistic (Sigmoid) Function — User Input Version
# No external libraries (only built-in math)
# ---------------------------------------------------------

import math

# Sigmoid function definition
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

print("🔹 Logistic (Sigmoid) Function 🔹")

# Take user input
x = float(input("Enter a value for x: "))

# Calculate sigmoid
y = sigmoid(x)

# Display result
print(f"\nSigmoid({x}) = {y:.6f}")

# Show a few example values for reference
print("\nSome example sigmoid values:")
for val in [-5, -2, 0, 2, 5]:
    print(f"Sigmoid({val:>2}) = {sigmoid(val):.6f}")
