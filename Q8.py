def is_valid_url(url):
    """
    Function to check if a given string is a valid URL.
    Uses only basic string operations, as per class instructions.

    :param url: The input string to check.
    :return: True if valid URL, False otherwise.
    """

    # Step 1: Check if the URL starts with "http://" or "https://"
    if not (url.startswith("http://") or url.startswith("https://")):
        return False

    # Step 2: Check if there's at least one dot (.)
    if "." not in url:
        return False

    # Step 3: Ensure there is something after the last dot (e.g., ".com")
    if url.rfind(".") == len(url) - 1:  # If dot is the last character
        return False

    return True  # If all checks pass, return True


# Testing the function
print(is_valid_url("http://example.com"))  # True
print(is_valid_url("https://my-site.org"))  # True
print(is_valid_url("ftp://wrong.com"))  # False (wrong protocol)
print(is_valid_url("http://invalid."))  # False (dot at the end)
print(is_valid_url("random_text"))  # False (not a URL)