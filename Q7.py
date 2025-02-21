import random

# Step 1: Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

print("Original list:", random_numbers)  # Print the original list

# Step 2: Remove odd numbers and double even numbers
i = 0  # Use an index variable since we are modifying the list
while i < len(random_numbers):
    if random_numbers[i] % 2 != 0:  # Check if the number is odd
        del random_numbers[i]  # Remove odd numbers
    else:
        random_numbers[i] *= 2  # Double the even numbers
        i += 1  # Move to the next index only if we didn't delete

# Step 3: Print the final modified list
print("Modified list (evens doubled, odds removed):", random_numbers)