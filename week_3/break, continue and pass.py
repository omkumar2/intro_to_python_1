email = input("Enter your email: ")
for c in email:
  if(c == "@"):
    break
  print(c, end ="")
print(c) 

# Enter your email: omkumar@gmail.com
# o m k u m a r 
# g m a i l . c o m

email = input("Enter your email: ")
for c in email:
  if(c == "@"):
    print("")
    continue
  print(c, end ="")
print(c) 

# Enter your email: omkumar@gmail.com
# o m k u m a r 
# g m a i l . c o m



#next
for x in range(11):
  if(x% 3 == 0 ):
    print(x)
  else:
    pass

# 0
# 3
# 6
# 9
