s="VIBGYOR"

for i in range(5):
  print(s[i])
 
# V
# I
# B
# G
# Y

s='VIBGYOR'
t='VIBGYOR'
#example of nested for loop
count=0
for i in range(7):
  for j in range(7):
    print(i,j,s[i],s[j])
    count=count+1

print("the total ways in which the two brothers can wear 7 different colours:",count)

#i=0 and j=0 print VV
#i=0 and j=1 print VI
#i=0 and j=2 print VB
#i=0 and j=3 print VG
#....
#i=0 and j=6 print VR
#i=1 and j=0 print IV