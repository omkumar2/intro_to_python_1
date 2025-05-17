import numpy as np

def uniform(n, m):
  return np.random.randint(1, n+1, size = m)

no = 0   #variable for storing number of event occurence
n = 60 #number of persons
print(1 - np.prod(1-np.arange(1,n)/365)) #probability from expression

for i in range(1000):
  B = np.zeros(366)   #array to keep track of birthdays seen
  for j in range(n): #generate birthdays for each person
    Bi = uniform(365, 1) #i-th birthday
    if B[Bi]  == 0:  #if Bi is seen for the first time
      B[Bi] = 1  #make note that Bi has been seen
    else:
      no = no + 1   #if Bi has been seen before, then two birthdays are same 
      break   #we can stop generating more birthdays and exit loop early

print(no/1000) #probability estimate by Monte Carlo