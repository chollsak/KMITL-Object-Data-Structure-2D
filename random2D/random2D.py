import random

# List of 39 numbers
all_numbers = list(range(1, 40))

# Generate 13 random numbers without replacement
random_numbers = random.sample(all_numbers, 13)

# Print the random numbers
print("Random 13 numbers:", random_numbers)
