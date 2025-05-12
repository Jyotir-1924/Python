def decorator(function):
    def wrapper():
        print("Inside wrapper (The new function)")
        function()
        print("Exiting wrapper (The new function)")
    return wrapper

def greet():
    print("Hello !")

f = decorator(greet)
f()

'''
New function f will look like this
def f():
    print("Inside wrapper")
    print("Hello !)
    print("Exiting wrapper")
'''