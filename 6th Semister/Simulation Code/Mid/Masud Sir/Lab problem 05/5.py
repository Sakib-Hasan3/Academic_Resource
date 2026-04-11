import math
import random
import matplotlib.pyplot as plt

# ----------------------------
# Poisson PMF Function
# ----------------------------
def poisson_pmf(lam, k):
    return (math.exp(-lam) * lam**k) / math.factorial(k)

# ----------------------------
# Print probabilities for λ = 5
# ----------------------------
lam = 5
print("Poisson Distribution (λ = 5 calls/hour)\n")

for k in range(0, 11):
    prob = poisson_pmf(lam, k)
    print(f"P(X = {k}) = {prob:.6f}")

# ----------------------------
# Plot PMF Graph Function
# ----------------------------
def plot_poisson(lam, max_k):
    x = list(range(0, max_k + 1))
    y = [poisson_pmf(lam, k) for k in x]

    plt.figure()
    plt.stem(x, y)
    plt.xlabel("Number of Calls per Hour")
    plt.ylabel("Probability")
    plt.title(f"Poisson PMF (λ = {lam})")
    plt.grid(True)
    plt.show()

# ----------------------------
# Graphs
# ----------------------------

# Graph for λ = 5 (0–10 calls)
plot_poisson(5, 10)

# Graph for λ = 10 (0–15 calls)
plot_poisson(10, 15)

# Graph for λ = 15 (0–15 calls)
plot_poisson(15, 15)