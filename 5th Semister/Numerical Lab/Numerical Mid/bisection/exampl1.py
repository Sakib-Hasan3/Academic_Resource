def bisection(f, a, b, tol=1e-6):
    # Check if the method is applicable
    if f(a) * f(b) >= 0:
        print("The bisection method is not applicable.")
        return None
    
    # Perform the bisection method
    while (b - a) / 2.0 > tol:
        m = (a + b) / 2.0  # Midpoint
        if f(m) == 0:  # If m is the root
            return m # Root is in the left half
        elif f(a) * f(m) < 0: 
            b = m
        else:  # Root is in the right half
            a = m
    
    # Return the midpoint as the root approximation
    return (a + b) / 2.0

# Define the function f(x) = x^2 - 3
def f(x):
    return x**2 - 3
 
# Find the root in the interval [1, 2]
root = bisection(f, 1, 2)
print(f"The root is approximately: {root}")
