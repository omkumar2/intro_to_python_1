
print("when did india get its independence (year)?")
year=int(input())

if(year==1947):
  print("hip hip hurray. you got that right!")
else:
  print("comeon dont you know even this?")
  print("that's ok, i will let you attempt this once more")
  print("when did india get its independence?")
  year=int(input())
  if(year==1947):
    print("you got it!")
  else:
    print("failed in your second attempt too? grrrr...")

#this code is write by while loop
print("when did india get its independence (year)?")
year=int(input())

while(year!=1947):
    print(year,"you got this wrong. enter once again")
    year=int(input())
print("woww...you got it right")

#while works like this:
   #while <condition>
   #write whatever you want here
   #write whatever you want here
   #write whatever you want here
   
   
#let us find the factorial of a number

print("Enter a number:")
n=int(input())
#n=5
#1*2*3*4*5
i=1
answer=1
while(i<=n):
   answer=answer*i
   i=i+1
print(answer)
