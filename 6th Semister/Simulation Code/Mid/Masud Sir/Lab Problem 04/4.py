import random

# Input values
n = int(input("Enter number of trials (n): "))
p = float(input("Enter probability of success (p): "))
simulations = int(input("Enter number of experiments: "))

results = []

# Run simulation
for _ in range(simulations):
    success_count = 0
    
    for i in range(n):
        r = random.random()
        if r < p:
            success_count += 1
            
    results.append(success_count)

# Display results
print("\nNumber of successes in each experiment:")
print(results)

# Calculate experimental mean
experimental_mean = sum(results) / simulations
theoretical_mean = n * p

print("\nExperimental Mean:", round(experimental_mean, 4))
print("Theoretical Mean (n*p):", round(theoretical_mean, 4))