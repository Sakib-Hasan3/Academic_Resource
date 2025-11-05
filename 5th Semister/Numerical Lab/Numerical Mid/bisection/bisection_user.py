# Step 1: Define the function
def f(x):
    return x**3 - 5*x + 3   # You can change this equation

# Step 2: Take user input
print("🔹 Bisection Method 🔹")
a = float(input("Enter lower bound (a): "))
b = float(input("Enter upper bound (b): "))
tol = float(input("Enter tolerance (e.g., 0.0001): "))
max_iter = int(input("Enter maximum iterations: "))

# Step 3: Check if initial guesses are valid
if f(a) * f(b) > 0:
    print("⚠️ Invalid interval! f(a) and f(b) must have opposite signs.")
else:
    print("\nIteration\t a\t\t b\t\t c\t\t f(c)")
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        print(f"{i}\t\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}")

        if abs(f(c)) < tol:
            print(f"\n✅ Root found at x = {c:.6f} after {i} iterations.")
            break

        # Update interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    else:
        print("\n⚠️ Maximum iterations reached without sufficient accuracy.")


#Enter lower bound (a): 0
#Enter upper bound (b): 1
#Enter tolerance (e.g., 0.0001): 0.0001
#Enter maximum iterations: 25