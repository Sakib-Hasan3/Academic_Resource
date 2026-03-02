import random
import math

# Input
n = int(input("Enter number of random variates: "))
lam = float(input("Enter lambda (rate parameter): "))

print("\nGenerated Random Variates:\n")

for i in range(n):
    u = random.random()              # Uniform(0,1)
    x = - (1/lam) * math.log(u)      # Inverse transform formula
    print(f"X{i+1} = {x:.6f}")