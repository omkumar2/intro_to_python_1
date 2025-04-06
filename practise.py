def is_present_in_opposite_halves(elem, l1: list, l2: list):
    """
    Determines whether an element is present in the first half of one list 
    and the second half of the other list, or vice versa.

    Args:
        elem (Any): The element to check for.
        l1 (list): The first list to search.
        l2 (list): The second list to search.

    Returns:
        bool: True if `elem` is present in opposite halves of `l1` and `l2`, 
        False otherwise.
    """
    mid1 = len(l1) // 2
    mid2 = len(l2) // 2

    # Check if elem is in the first half of l1 and the second half of l2
    in_first_half_l1 = elem in l1[:mid1]
    in_second_half_l2 = elem in l2[mid2:]
    
    # Check if elem is in the second half of l1 and the first half of l2
    in_second_half_l1 = elem in l1[mid1:]
    in_first_half_l2 = elem in l2[:mid2]

    return (in_first_half_l1 and in_second_half_l2) or (in_second_half_l1 and in_first_half_l2)


print(is_present_in_opposite_halves(3, [1, 2, 3, 4], [3, 4, 5, 6]))

# next question 

def count_odd_three_digit_nums(nums):
    count = 0
    for num in nums:
        if num is not None:
            if (100 <= abs(num) <= 999 and num % 2 == 1):
                count = count + 1
    return count 
    
    
def count_odd_three_digit_nums(nums):
    count = 0
    for num in nums:  # Add loop to check each number
        if num is not None:  # Check for None values
            if (100 <= abs(num) <= 999 and  # Check each number individually
                num % 2 == 1 and  # Check if odd
                isinstance(num, int)):  # Ensure it's an integer
                count = count + 1
    return count    
    
#next question

# Read number of names
n = int(input())

# List to store the formatted names
formatted_names = []

# Read each name and process it
for _ in range(n):
    full_name = input().strip().split()
    # Extract last name
    last_name = full_name[-1]
    # Extract initials (all parts except the last)
    initials = [name[0] + '.' for name in full_name[:-1]]
    # Join initials with last name
    formatted_name = ' '.join(initials + [last_name])
    formatted_names.append(formatted_name)

# Sort the formatted names alphabetically
formatted_names.sort()

# Print each formatted name
for name in formatted_names:
    print(name)


# next question



def sum_of_floored_to_tens(a:int, b:int):
    """
    Calculate the sum of two integers floored to the nearest lower multiple of 10.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers after flooring each to the nearest lower multiple of 10.

    Examples:
        >>> sum_of_floored_to_tens(23, 47)
        60
        >>> sum_of_floored_to_tens(35, 19)
        40
        >>> sum_of_floored_to_tens(0, 105)
        100
    """
    return ((a // 10)*10) + ((b // 10)*10)

print(sum_of_floored_to_tens(23, 47))

# next question

def surround_first_two_and_last_two_with_brackets(s: str):
    """
    Surrounds the first two and last two characters of the input string with square brackets.

    It is assumed that the input has atleast four characters.

    Args:
        s (str): The input string.

    Returns:
        str: A new string with the first two and last two characters surrounded by square brackets.

    Example:
        >>> surround_first_two_and_last_two_with_brackets("example")
        '[ex]amp[le]'
    """
    # return f"[{s[:2]}]{s[2:-2]}[{s[-2:]}]"
    return f"[{s[:2]}]{s[2:-2]}[{s[-2:]}]"

print(surround_first_two_and_last_two_with_brackets("example"))

# next question

def number_with_more_unique_digits(n1:int, n2:int):
    """
    Compares two integers and returns the one with more unique digits.

    Args:
        n1 (int): The first integer.
        n2 (int): The second integer.

    Returns:
        int or tuple: The integer with more unique digits. 
        If both numbers have the same number of unique digits, 
        returns a tuple of both integers `(n1, n2)`.

    Example:
        >>> number_with_more_unique_digits(123, 1122)
        123

        >>> number_with_more_unique_digits(1122, 2211)
        (1122, 2211)
    """
    unique_n1 = len(set(str(n1)))
    unique_n2 = len(set(str(n2)))
    
    # Compare counts of unique digits
    if unique_n1 > unique_n2:
        return n1
    elif unique_n2 > unique_n1:
        return n2
    else:
        return (n1, n2)
    
#next question

def count_vowels_and_consonants_in_even_indices(s: str) -> tuple:
    """
    Counts the number of vowels and consonants at even indices in the given string.

    Args:
        s (str): The input string.

    Returns:
        tuple: A tuple containing two integers:
            - The first integer is the count of vowels at even indices.
            - The second integer is the count of consonants at even indices.

    Example:
        >>> count_vowels_and_consonants_in_even_indices("example1")
        (3, 1)

        >>> count_vowels_and_consonants_in_even_indices("hello")
        (1, 2)
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for i in range(0, len(s), 2):  # Only even indices
        if s[i].isalpha():  # Check if it's a letter
            if s[i] in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return (vowel_count, consonant_count)

#next question


def product_of_sum_and_abs_diff_of_digits(num: int):
    """Returns the product of the sum and absolute difference of digits of a two digit number.

    Assume number is a two digit number.

    Args:
        num (int) - The given number

    Returns:
        The required product.

    Examples:
        >>> product_of_sum_and_abs_diff_of_digits(38)
        55
        >>> product_of_sum_and_abs_diff_of_digits(55)
        0
    """
    # Extract digits
    tens = num // 10
    ones = num % 10

    # Calculate sum and absolute difference
    digit_sum = tens + ones
    digit_diff = abs(tens - ones)

    # Return the product
    return digit_sum * digit_diff
    
    
print(product_of_sum_and_abs_diff_of_digits(38))


# next 


def is_divisible_by_last_two_digits(num: str):
    """
    Checks if the given number is divisible by both of its last two digits.

    Return False if any of the last two digits is 0.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if divisible by both last two digits, False otherwise.
    """
    # Convert to string to easily access digits
    num_str = str(num)

    # Get the last two digits
    last_two_digits = num_str[-2:]

    # Check if any of the last two digits is '0'
    if '0' in last_two_digits:
        return False

    # Convert last two digits to integers
    last_digit1 = int(last_two_digits[0])
    last_digit2 = int(last_two_digits[1])

    # Check divisibility
    return (num % last_digit1 == 0) and (num % last_digit2 == 0)

#next 

# This writes the stdin to the input file
import tempfile
import sys
_ , filename = tempfile.mkstemp(prefix="case")
with open(filename, 'w') as f:
  f.write(sys.stdin.read())
  

with open(filename) as f:
    vowel_count = 0
    for line in f:
        for char in line:
            if char in 'aeiou':
                if vowel_count % 2 == 0:
                    print("ub", end="")
                else:
                    print("dub", end="")
                vowel_count += 1
            print(char, end="")

#next question

