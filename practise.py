

def has_a_in_second_half(s: str) -> bool:
    '''
    Given an even-length string, check if the second half contains 
    the character "a" or "A".

    Arguments:
    s: str - an even-length string.

    Return: bool - True if "a" or "A" is found in the second half, else False.
    '''
    half = 0
    for half in range(len(s)):
        if half // 2 == 0:
            return "a" in second_half or "A" in second_half
    
    if len(s) % 2 != 0:
        return False  # Could raise an error instead, depending on requirements
    
    # Find the midpoint
    mid = len(s) // 2
    
    # Get the second half
    second_half = s[mid:]
    
    # Check if "a" or "A" is in the second half
    return "a" in second_half or "A" in second_half
