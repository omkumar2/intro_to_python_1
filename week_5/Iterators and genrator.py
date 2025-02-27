fruits = ['mango', 'apple', 'banana', 'orange', 'pineapple', 'watermelon', 'guava', 'kiwi']

bascket = iter(fruits)
print(bascket)
print(next(bascket))
print(next(bascket))
print(next(bascket))
print(next(bascket))
print(next(bascket))
print(next(bascket))
print(next(bascket))


def square(Limit):
    x=0
    while x<Limit:
        yield x*x
        yield x*x*x
        x+=1
        
a = square(5)
print(next (a),next(a))
print(next (a),next(a))
print(next (a),next(a))