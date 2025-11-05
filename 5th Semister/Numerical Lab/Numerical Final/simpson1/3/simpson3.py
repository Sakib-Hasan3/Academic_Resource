# f(x) সংজ্ঞা
def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

# Simpson’s 1/3 Rule (single panel)
def simpsons_1_3(f, a, b):
    m = (a + b) / 2.0
    return (b - a) * (f(a) + 4*f(m) + f(b)) / 6.0

# Composite Simpson’s 1/3 Rule: n সাব-ইন্টারভ্যাল (n অবশ্যই জোড় সংখ্যা)
def composite_simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Composite Simpson’s 1/3.")
    h = (b - a) / n
    s = f(a) + f(b)
    # 4 গুণক: odd indices
    for i in range(1, n, 2):
        s += 4 * f(a + i*h)
    # 2 গুণক: even indices
    for i in range(2, n, 2):
        s += 2 * f(a + i*h)
    return s * h / 3.0

# সীমা
a, b = 0.0, 0.8

# Single-panel Simpson
single = simpsons_1_3(f, a, b)
print(f"Single Simpson’s 1/3 on [{a}, {b}]  = {single:.6f}")

# Composite Simpson (e.g., n = 100, even)
n = 100
comp = composite_simpson(f, a, b, n)
print(f"Composite Simpson’s 1/3 (n={n})     = {comp:.6f}")
