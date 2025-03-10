print("v shape")


n = int(input())
for i in range(n-1):
    print(f"{' '*i}\\{' '*(2*(n-i)-3)}/")
print(' '*(n-1)+'v')



n = int(input())
for i in range(1, n + 1):
    if i < n:
        print(' ' * (i - 1) + '\\' + ' ' * (2 * (n - i) - 1) + '/')
    else:
        print(' ' * (n - 1) + 'v')
        


print("x shape") 

n = int(input())
for i in range(n):
    print(f"{' '*i}\\{' '*(2*(n-i)-1)}/")
print(f"{' '*n}x")
for i in range(n-1,-1,-1):
    print(f"{' '*i}/{' '*(2*(n-i)-1)}\\")
    
    

n = int(input())
# Top half
for i in range(1, n + 1):
        print( ' ' * (i - 1) + '\\' +  ' ' * (2 * (n - i) + 1) + '/')
# Center
print(' ' * n + 'x')
# Bottom half
for i in range(n, 0, -1):
    print( ' ' * (i - 1) + '/' +  ' ' * (2 * (n - i) + 1) + '\\')
    
    
print("w shape")
    
n = int(input())
for i in range(n, 0, -1):
    print( '|'+' ' * (i - 1) + '/' +  ' ' * (2 * (n - i) +0) + '\\' + ' ' * (i - 1) + '|')
    
    
    
n = int(input())
for i in range(n-1,-1,-1):
   print(f"|{' '*i}/{' '*(2*(n-i)-2)}\\{' '*(i)}|")
    
    
print("z shape")
    
n = int(input())
for i in range(n, n-1,-1):
    print(f"{'*'*n}")
for i in range(n-1,1,-1):
    print(f"{' '*(i-1)}*")
for i in range(n, n-1,-1):
    print(f"{'*'*n}")
    
    


n = 4
for i in range(n,0,-1):
    print(f"{' '*(i-1)}{'0 '*(n-(i-1))}") 

    
    

n =int(input())
for i in range(n,0,-1):
    print(f"{' 0 '*(n-(i-1))}") 

    
    

n = int(input())
for i in range(n,0,-1):
    print(f"{' '*(i-1)}{'0'*(n-(i-1))}") 

    
    
n = int(input())

for i in range(n):
    spaces = ' ' * (n - i - 1)  # Leading spaces to center the triangle
    zeros = ' '.join('0' * (i + 1))  # Creating the row with spaces between zeros
    print(spaces + zeros)


n = int(input())
for i in range(n,0,-1):
    print(f"{' '*(i-1)}{' 0'*(n-(i-1))}") 
    
    

    
    
    
# star pattern

n = 5
for i in range(n,0,-2):
    print(f"{' '*(n-(i))}{'*'*(n-(i-1))}")







#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *







#   *
#  ***
# *****
#  ***
#   *

