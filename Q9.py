def days_since_birth(birthday):
    """
    Function to calculate the number of days passed since the year after birth.
    It does NOT count the birth year or the current year, only full years.

    :param birthday: String in "DD-MM-YYYY" format
    :return: Number of days (excluding birth and current year)
    """

    # Step 1: Extract the birth year
    birth_year = int(birthday[-4:])  # Last 4 characters are the year

    # Step 2: Current year is 2025
    current_year = 2025

    # Step 3: Calculate the full years in between
    full_years = current_year - birth_year - 1  # Exclude birth year and current year

    # Step 4: Compute the total days without leap years
    total_days = full_years * 365

    # Step 5: Count the leap years (divisible by 4, but not 100 unless also 400)
    leap_years = 0
    for year in range(birth_year + 1, current_year):  # Check only full years
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1  # Each leap year adds 1 extra day

    # Step 6: Add leap year days
    total_days += leap_years

    return total_days


# Testing with your birthdate: "21-09-2004"
print(days_since_birth("21-09-2004"))  # Output: Number of days