a=int(5.7)
b=int("10")

print(a, type(a)) #5<class 'int'>
print(b, type(b)) #10 <class 'int'>

c=float(5)
d=float("1.4")

print(c, type(c)) #5.0 <class 'float'>
print(d, type(d)) #1.4 <class 'float'>

e=str(5.3)
f=str(1)

print(e, type(e)) #5.3 <class 'str'>
print(f, type(f)) #1 <class 'str'>

g=bool(1)
h=bool(0)
i=bool(-1)

print(g, type(g)) #True <class 'bool'>
print(h, type(h)) #False <class 'bool'>
print(i, type(i)) #True <class 'bool'>

j=bool(10.5)
k=bool(0.0)
l=bool(-10.6)

print(j, type(j)) #True <class 'bool'
print(k, type(k)) #False <class 'bool'>
print(l, type(l)) #True <class 'bool'>


a=bool("india")
b=bool("10")
c=bool("-10.5")
d=bool("0")
e=bool("")

print(a,type(a)) #True <class 'bool'>
print(b,type(b)) #True <class 'bool'>
print(c,type(c)) #True <class 'bool'>
print(d,type(d)) #True <class 'bool'>
print(e,type(e)) #False <class 'bool'>