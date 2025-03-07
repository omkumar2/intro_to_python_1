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
    
    
    

n = int(input())
for i in range(n):
    print(f"|{' '*i}\\{' '*(n-i-1)}|")
    
