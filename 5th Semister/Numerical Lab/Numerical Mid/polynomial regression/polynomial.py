# Minimal Polynomial Regression (pure Python, degree=4)

def f(x): 
    return 3*x**4 - 7*x**3 + 2*x**2 + 11  # ground-truth function

# build data
x = [float(t) for t in range(30)]
y = [f(t) for t in x]

def polyfit_pure(x, y, d):
    # Vandermonde
    V = [[xi**k for k in range(d+1)] for xi in x]
    VT = list(zip(*V))  # transpose (as tuples)

    # Normal equations: (VT V) a = (VT y)
    A = [[sum(VT[r][i]*VT[c][i] for i in range(len(x))) for c in range(d+1)] for r in range(d+1)]
    b = [sum(VT[r][i]*y[i]      for i in range(len(x))) for r in range(d+1)]

    # Gauss–Jordan solve
    n = len(A)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        piv = M[c][c]
        for j in range(c, n+1): M[c][j] /= piv
        for r in range(n):
            if r == c: continue
            fct = M[r][c]
            for j in range(c, n+1): M[r][j] -= fct * M[c][j]
    return [M[i][n] for i in range(n)]  # a0..ad

# fit degree-4
a = polyfit_pure(x, y, 4)

# predict (Horner)
def predict(xv, a=a):
    s = 0.0
    for k in range(len(a)-1, -1, -1):
        s = s * xv + a[k]
    return s

print("Coefficients a0..a4:", [round(v, 6) for v in a])
for xv in [0, 5, 10, 15, 20, 25, 29]:
    print(f"x={xv:>2}  y_pred={predict(float(xv)):.3f}  y_true={f(float(xv)):.3f}")
