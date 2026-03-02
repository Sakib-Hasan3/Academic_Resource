# ---------------------------------
# Linear Congruential Generator
# ---------------------------------

# Input parameters
a = 5          # multiplier
c = 3          # increment
m = 16         # modulus
seed = 7       # initial value (X0)
n = 10         # how many random numbers to generate

# First value
X = seed

print("LCG Random Numbers:")
print("---------------------")

for i in range(n):
    X = (a * X + c) % m
    U = X / m   # Convert to (0,1)
    print(f"X{i+1} = {X}   |   U{i+1} = {U:.4f}")