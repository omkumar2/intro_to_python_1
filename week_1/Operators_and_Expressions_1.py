a=12
b=3.3
n=a+b
print(n) #15.3

a='jay'
b='om'
n=a*b
print(n) #error

a='jay'
b='om'
n=a+b
print(n) #jayom

a=[1,2,3]
b=[7,9,12]
n=a+b
print(n) #[1,2,3,9,12]

n=10+13*2
#my guess is n will be 46.
#the expected answer was incorrect. the correct answer is 36. That is due to what is called the operator precedence.
print(n)

n=((10+13)*2) # is 46
print(n)