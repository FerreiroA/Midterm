# List Example (Mutable)
my_list = [1, 2, 3]
print("Original list:", my_list)

my_list[0] = 100  # Changing the first element
print("Modified list:", my_list)  # List is changed

# String Example (Immutable)
my_string = "hello"
print("\nOriginal string:", my_string)

# Trying to modify a character (will cause an error)
try:
    my_string[0] = "H"  # This is NOT allowed in Python
except TypeError as e:
    print("Error:", e)

# Correct way to modify a string (Create a new one)
new_string = "H" + my_string[1:]
print("Modified string:", new_string)  # Creates a new string