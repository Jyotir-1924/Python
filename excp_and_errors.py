def sum(a,b):
    try:
        c = a/b
        return (f"The answer is {c} ! Successful")

    except Exception as err:
        return (f"Error caused as {err} ! Retry :)")
    
    finally:
        print("Hey, this is executed at end inside finally")
    #This print statement becomes redundant. It will not be printed !
    print("This is a simple print statement !")
    
while True:
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    print(sum(num1,num2))