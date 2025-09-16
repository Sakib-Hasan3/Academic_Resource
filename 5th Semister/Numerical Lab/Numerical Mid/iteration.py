import math 
def f(x):
    return math.cos(x)

def fixed_point(x0, tol=1e-5, max_iter=100):
    x=x0
    for i in range(max_iter):
        x_new=f(x)
        if abs(x_new -x) <tol:
            print(f"solution x={x_new:0.6f} converged in {i} iterations")
            return x_new
        x=x_new
        print("solution not converge")
        return None
fixed_point(x0=0.5)
  