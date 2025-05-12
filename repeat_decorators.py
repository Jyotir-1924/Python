def repeat(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return decorator

@repeat(10)
def greet(token):
    print(f"Hello {token}!")
    
greet("Jyotiraditya")

'''
This function will execute like
def repeat(10):
    def decorator(greet):
        def wrapper("Jyotir"):
            for i in range(10):
                print("Hello Jyotiraditya!")
        return wrapper
    return decorator

An example of the nested functions !

'''