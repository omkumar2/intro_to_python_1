

# def has_a_in_second_half(s: str) -> bool:
#     '''
#     Given an even-length string, check if the second half contains 
#     the character "a" or "A".

#     Arguments:
#     s: str - an even-length string.

#     Return: bool - True if "a" or "A" is found in the second half, else False.
#     '''
#     if len(s) % 2 != 0:
#         return False  # Could raise an error instead, depending on requirements
    
#     # Find the midpoint
#     mid = len(s) // 2
    
#     # Get the second half
#     second_half = s[mid:len(s)-1]
    
#     # Check if "a" or "A" is in the second half
#     return "a" in second_half or "A" in second_half

# print(has_a_in_second_half("abcde"))  # False
# print(has_a_in_second_half("abcdea"))  # True


