a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
try:
    c = a / b
    print("The result is:", c)
    f = open('abc.txt', 'r')
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except NameError:
    print("Error: Variable 'd' is not defined.")
except FileNotFoundError:
    print("Error: The file 'abc.txt' was not found.")   
except :
    print("somthing went worng")   
 
 
# this is code
 
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
try:
    f = open('abc.txt', 'r')
    c = a / b
    print("The result is:", c)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except :
    print("somthing went worng")   
finally:
    f.close()
    print("From Finally block")
    
    
# this is code create my own exception 

a = int(input())
if a < 18:
    raise Exception("You are not eligible to vote.")
    