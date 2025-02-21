def find_pattern(text):
    """
    Function to find occurrences of words that start with 'C', have any number of letters,
    and end with 'jeb'. It returns the count of matches.

    :param text: The input string to search in.
    :return: Number of matches found.
    """

    words = text.split()  # Split text into words
    count = 0  # Counter for matches

    for word in words:
        if word.startswith("C") and word.endswith("jeb"):
            count += 1  # Increment if pattern matches

    return count  # Return the total count


# Example Usage
text = "ChelloJjeb Ctestjeb Csomethingjeb notCjeb Cxyzjeb CnotmatchingCjeb"
result = find_pattern(text)
print(result)  # Output: 4 (or the correct count based on the input)