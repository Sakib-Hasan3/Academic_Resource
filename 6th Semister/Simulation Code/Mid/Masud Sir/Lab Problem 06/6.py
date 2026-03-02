import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# -----------------------------
# 1. Unimodal Normal Curve
# -----------------------------
mean1 = 100
sd1 = 20

x = np.linspace(0, 200, 500)
y = norm.pdf(x, mean1, sd1)

plt.figure()
plt.plot(x, y)
plt.title("Unimodal Normal Distribution (Mean=100, SD=20)")
plt.xlabel("X")
plt.ylabel("Density")
plt.grid(True)
plt.show()


# -----------------------------
# 2. Multimodal Normal Curve
# -----------------------------
mean2 = 80
mean3 = 120
sd2 = 15

y1 = norm.pdf(x, mean2, sd2)
y2 = norm.pdf(x, mean3, sd2)

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Multimodal Normal Distribution")
plt.xlabel("X")
plt.ylabel("Density")
plt.grid(True)
plt.show()


# -----------------------------
# 3. Random Sample (n = 200)
# -----------------------------
sample = np.random.normal(100, 20, 200)

plt.figure()
plt.hist(sample, bins=15, density=True)
plt.title("Histogram of Random Sample (Mean=100, SD=20)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.show()


# -----------------------------
# 4. Diastolic Blood Pressure
# -----------------------------
bp_sample = np.random.normal(80, 20, 200)

plt.figure()
plt.hist(bp_sample, bins=15, density=True)
plt.title("Diastolic Blood Pressure Distribution")
plt.xlabel("Blood Pressure")
plt.ylabel("Density")
plt.grid(True)
plt.show()