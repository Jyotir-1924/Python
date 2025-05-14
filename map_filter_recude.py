from functools import reduce 
numbers = [1,2,3,4,5,6,7,8,9,10]

def reduceFunc(a,b):
    return a+b

l1 = list(map(lambda x : x+10, numbers))

l2 = list(filter(lambda x : x%2==0, numbers))

l3 = reduce(reduceFunc, numbers)

print(l1)
print(l2)
print(l3)

#This is a demonstration of higher order functions map, reduce and filter.