
def f(x):
    return x**3 - 5*x + 3   # Example: f(x) = x³ - 5x + 3

# Step 2: Define inputs directly in the code
a = 0          # lower bound
b = 1          # upper bound
tolerance = 0.0001
max_iterations = 25

# Step 3: Check validity of interval
if f(a) * f(b) > 0:
    print("⚠️ Invalid interval! f(a) and f(b) must have opposite signs.")
else:
    print("🔹 Bisection Method 🔹")
    print("\nIteration\t   a\t\t     b\t\t     c\t\t    f(c)")
    
    for i in range(1, max_iterations + 1):
        c = (a + b) / 2
        fc = f(c)
        
        # Print each iteration
        print(f"{i:>3}\t {a:10.6f}\t {b:10.6f}\t {c:10.6f}\t {fc:10.6f}")
        
        # Stop when tolerance satisfied
        if abs(fc) < tolerance:
            print(f"\n✅ Root found at x = {c:.6f} after {i} iterations.")
            break
        
        # Update bounds
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    else:
        print("\n⚠️ Maximum iterations reached without desired accuracy.")
