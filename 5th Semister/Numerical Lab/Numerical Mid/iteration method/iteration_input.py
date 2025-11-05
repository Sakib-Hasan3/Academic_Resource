# Iteration Method (Successive Approximation) for: x^3 + x - 1 = 0
# Convergent mapping: x = 1 / (1 + x^2)

def g(x):
    # Better fixed-point form that converges for this equation
    return 1 / (1 + x**2)

def iteration_method(x0, tol=1e-6, max_iter=100):
    print("\nIteration\t x_n\t\t x_(n+1)\t\t |x_(n+1) - x_n|")
    for i in range(max_iter):
        x1 = g(x0)
        error = abs(x1 - x0)
        print(f"{i+1}\t\t {x0:.6f}\t {x1:.6f}\t {error:.6f}")
        if error < tol:
            print(f"\n✅ Root found at x = {x1:.6f} after {i+1} iterations.")
            return x1
        x0 = x1
    print("\n⚠️ Maximum iterations reached without convergence.")
    return x1

# -------- Main Program --------
print("🔹 Iteration Method (Successive Approximation) 🔹")
x0 = float(input("Enter initial guess x0: "))
iteration_method(x0)
