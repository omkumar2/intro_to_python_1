def f(n):
    if n > 1:
        if (n ** 0.5) == int(n ** 0.5):
            return 1 + f(int(n ** 0.5))
        elif n % 2 != 0:
            return 1 + f(3 * n + 1) 
        else:
            return 1 + f(int(n / 2))
    elif n < 1:
        return 1 + f(n ** 2)
    else:
        return 0
                
print(f(10000))

# next

class test:
    def __init__(self):
        self.variable = 'Old'
        self.Change(self.variable)
    def Change(self, var):
        var = 'New'
obj = test()
print(obj.variable)

# next

a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5, 6, 7]
L = list(map(lambda n, m: m * n, a, b))

print(L) 