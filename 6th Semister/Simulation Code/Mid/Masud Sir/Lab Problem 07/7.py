import numpy as np
import matplotlib.pyplot as plt
import math

# -----------------------------------
# Part 1: Probability Calculation
# -----------------------------------

mean_days = 100
lam = 1 / mean_days     # rate

t = 120

prob = math.exp(-lam * t)

print("Rate (lambda):", lam)
print("P(X > 120 days) =", round(prob, 6))


# -----------------------------------
# Part 2: Simulation of Exponential
# -----------------------------------

rates = [0.5, 1.0, 2.0, 4.0]

plt.figure()

for r in rates:
    sample = np.random.exponential(1/r, 1000)   # scale = 1/lambda
    plt.hist(sample, bins=40, density=True, alpha=0.5, label=f"λ={r}")

plt.title("Exponential Distribution Simulation")
plt.xlabel("Time")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()