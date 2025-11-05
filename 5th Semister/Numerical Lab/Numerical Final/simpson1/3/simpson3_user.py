# ---------------------------------------------------------
# Simpson’s 1/3 Rule (Pure Python, with User Input)
# ---------------------------------------------------------

# Step 1: Define the function
def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

# Step 2: Take user inputs
print("🔹 Simpson’s 1/3 Rule 🔹")
a = float(input("Enter lower limit (a): "))
b = float(input("Enter upper limit (b): "))
n = int(input("Enter number of subintervals (even number): "))

# Check if n is even
if n % 2 != 0:
    print("⚠️ n must be an even number for Simpson’s 1/3 Rule.")
else:
    # Step 3: Apply Simpson’s 1/3 Rule
    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n):
        x = a + i*h
        if i % 2 == 0:
            s += 2 * f(x)
        else:
            s += 4 * f(x)

    result = (h / 3) * s

    # Step 4: Display results
    print(f"\n✅ Simpson’s 1/3 Rule Approximation = {result:.6f}")
