import random

# Input probability of success
p = float(input("Enter probability of success (0 to 1): "))

# Number of trials
n = int(input("Enter number of trials: "))

success = 0
results = []

for i in range(n):
    r = random.random()   # random number between 0 and 1
    
    if r < p:
        results.append(1)   # success
        success += 1
    else:
        results.append(0)   # failure

print("\nResults (0 = failure, 1 = success):")
print(results)

print("\nTotal Success:", success)
print("Total Failure:", n - success)
print("Experimental Probability:", success / n)