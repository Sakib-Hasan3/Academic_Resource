# False Position (Regula Falsi) Method in Python

def f(x):
    # Fixed Equation
    return x**3 - 5*x + 3   # Equation: f(P) = P^3 - 5P + 3

def false_position(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) > 0:
        print("⚠️ No root found in the given interval. f(a) and f(b) must have opposite signs.")
        return None
    
    print("\nIteration\t a\t\t b\t\t c\t\t f(c)")
    for i in range(max_iter):
        # Apply False Position formula
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        
        print(f"{i+1}\t\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}")
        
        # Check for convergence
        if abs(f(c)) < tol:
            print(f"\n✅ Root found at x = {c:.6f} after {i+1} iterations.")
            return c
        
        # Update interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    print("\n⚠️ Maximum iterations reached without sufficient accuracy.")
    return c


# -------- Main Program --------
print("🔹 False Position Method (User Input for a and b) 🔹")

# Take user input for a and b
a = float(input("Enter the first guess a: "))
b = float(input("Enter the second guess b: "))

# Call the function
root = false_position(a, b)


# example usage:
# a=0
# b=1