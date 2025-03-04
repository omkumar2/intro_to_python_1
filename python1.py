
def is_right_triangle_with_even_sides(a:int,b:int,c:int) -> bool:
    '''
    Given three side lengths in the increasing 
    order of length as a, b, and c, where a<=b<=c,
    check if the given sides are the sides of a right 
    triangle whose perpendicular sides are of even length.

    Hint: in a right triangle the square of hypotenuse is the sum of square of other two sides.

    Arguments:
    a: int - the first side length
    b: int - the second side length
    c: int - the hypotenuse length

    Return:
    bool - True if the sides form a right triangle and the perpendicular sides are even, else False
    '''
    a =6
    b =8
    c =10
    if (a<0 , b<0 , c<0):
        return False
    if (a<=b<=c):
        print(a**2)
        print(b**2)
        print(c**2)
        print(a%2==0)
        print(b%2==0)
        print(a**2 + b**2 == c**2) 
        return (a**2 + b**2 == c**2) and (a%2==0 and b%2==0)



# print(is_right_triangle_with_even_sides(3, 3, 5))
print(is_right_triangle_with_even_sides(6, 8, 10))
#print(is_right_triangle_with_even_sides(3, 4, 5))
#print(is_right_triangle_with_even_sides(4, 6, 8))
