# ---------------------------------------------------------
# Simpson’s 3/8 Rule (Pure Python, No Libraries)
# ---------------------------------------------------------

# Step 1: Define the function f(x)
def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

# Step 2: Simpson’s 3/8 rule formula
def simpsons_3_8(f, a, b):
    h = (b - a) / 3
    result = (3 * h / 8) * (f(a) + 3*f(a + h) + 3*f(a + 2*h) + f(b))
    return result

# Step 3: Inputs (already in the code)
a = 0.0   # lower limit
b = 0.8   # upper limit

# Step 4: Call the function
result = simpsons_3_8(f, a, b)

# Step 5: Display the result
print("🔹 Simpson’s 3/8 Rule 🔹")
print(f"Lower limit (a): {a}")
print(f"Upper limit (b): {b}")
print(f"\n✅ Simpson’s 3/8 Rule Result = {result:.6f}")

# Step 6: Show sample values for understanding
print("\nSample f(x) values:")
for x in [a, a + (b - a)/3, a + 2*(b - a)/3, b]:
    print(f"x = {x:.4f} → f(x) = {f(x):.6f}")
