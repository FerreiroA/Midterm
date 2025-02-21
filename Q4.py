# Function to check if a string (number) is a palindrome
def palindrome(word):
    return word == word[::-1]

# Given options
options = {
    "A": "2704702208931031198668911301398022074072",
    "B": "0974101607733149676776769413377061014790",
    "C": "4257304920394478392772938744930294037524",
    "D": "7798338247658278460338648728567428338977"
}

# Checking which number is NOT a palindrome
for key, value in options.items():
    if not palindrome(value):
        print(f"Option {key} is NOT a palindrome: {value}")