def sum(*args): 
    total = 0
    for item in args:
        total += item 
    return total

def marks(**kwargs):
    
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(1, 2, 4, 5, Jack=34, Jill=32, Marie=31)

marks(Shubham=34, Vikrant=54, Jack=34, Marie=90, Priya=45)

print(sum(342, 2, 7, 9))

# kwargs is a dictionary with all the key value pairs which were passed to marks
# args will be a tuple of all the values passed to sum
# kwargs is a dictionary with all the key value pairs which were passed to func1
# args and kwargs are used to pass a variable number of arguments to a function
# args should be used first and kwargs should be used second
# The output of the above code will be:
# (1, 2, 4, 5)
# {'Jack': 34, 'Jill': 32, 'Marie': 31}
# The marks of Shubham is 34
# The marks of Vikrant is 54
# The marks of Jack is 34
# The marks of Marie is 90
# The marks of Priya is 45