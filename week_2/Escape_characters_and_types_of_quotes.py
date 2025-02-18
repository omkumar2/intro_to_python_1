#Escape characters 
#print('It's a beautiful day') #error
print('It\'s a beautiful day') #it's a beautiful day  , and \ this is a escape characters
print("We are from \"IIT\" Madras") #We are from "IIT" Madras
print('We are from "IIT" Madras') #We are from "IIT" Madras

#next
print('My name is Om. \t\tI am from darbhanga') #My name is Om.      I am from darbhanga , \t this escape character put gape
print('My name is Om. \nI am from darbhanga') #My name is Om. 
                                              #I am from darbhanga ,  \n this is a escape charater that put in next line

#next
x = 'this is a string'
y = "this is also a string"
z = '''first line
second line
third line'''
print(x) #this is a string
print(y) #this is also a string
print(z) #'''this command is used for if a sentence is in next line even than there will no error

#next
#String Methods
x='pytHoN sTrIng MEthOdS'
print(x.lower()) #python string methods
print(x.upper()) #PYTHON STRING METHODS
print(x.capitalize()) #Python string methods
print(x.title()) #Python String Methods
print(x.swapcase()) #PYThOn StRiNG meTHoDs

#next
x = 'python'
print(x.islower()) #true
x = 'Python'
print(x.islower()) #false
x = 'PYTHON'
print(x.isupper()) #true
x = 'PyThOn'
print(x.isupper()) #false
x = 'Python String Methods'
print(x.istitle()) #true
x = 'Python string methods'
print(x.istitle()) #false

#next
x = '123'
print(x.isdigit()) #ture
x = '123abc'
print(x.isdigit()) #false
x = 'abc'
print(x.isalpha()) #ture
x = 'abc123'
print(x.isalpha()) #false
x = 'abc123'
print(x.isalnum()) #true
x = 'abc123!@#'
print(x.isalnum()) #false

#next
x = '-----python-----'
print(x.strip('-')) #python
print(x.lstrip('-')) #python-----
print(x.rstrip('-')) #-----python

#next
x = 'Python'
print(x.startswith('P')) #true
print(x.startswith('p')) #false
print(x.endswith('n')) #true
print(x.endswith('N')) #false

#next
x = "Python String Methods"
print(x.count("t")) #3
print(x.count("s")) #1
print(x.index("t")) #2
print(x.index("s")) #20
x = x.replace("S", "s")
x = x.replace("M", "m")
print(x) #Python string methods