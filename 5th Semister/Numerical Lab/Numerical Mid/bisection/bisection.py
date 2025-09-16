def bisection(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        print("The bisection method is not applicable.")
        return None
    
    while (b - a) / 2.0 > tol:
        m = (a + b) / 2.0
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2.0
