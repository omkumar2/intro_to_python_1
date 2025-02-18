alpha='abcdefghijklmnopqrstuvwxyz'

i=1
print(alpha[i]) #b
print(alpha[i+1]) #c
print(alpha[i+2]) #d

#next
alpha='abcdefghijklmnopqrstuvwxyz'

i=24
print(i%26) #24
print(alpha[i%26]) #y
print(alpha[(i+1)%26]) #z
print(alpha[(i+2)%26]) #a

#next
alpha='abcdefghijklmnopqrstuvwxyz'

o='omkumar'
#i expect to output tvebstibo
t=''

print(alpha.index(o[0])) #14
print(((alpha.index(o[0]))+1)%26) #15
print(alpha[((alpha.index(o[0]))+1)%26]) #p
t=t+(alpha[((alpha.index(o[0]))+1)%26]) 
print(t) #p

i=0
k=2
t=t+(alpha[(((alpha.index(o[i]))+k)%26)])
t=t+(alpha[(((alpha.index(o[i+1]))+k)%26)])
t=t+(alpha[(((alpha.index(o[i+2]))+k)%26)])
t=t+(alpha[(((alpha.index(o[i+3]))+k)%26)])
t=t+(alpha[(((alpha.index(o[i+4]))+k)%26)])
t=t+(alpha[(((alpha.index(o[i+5]))+k)%26)])
t=t+(alpha[(((alpha.index(o[i+6]))+k)%26)])
print(t) #pqomwoct
