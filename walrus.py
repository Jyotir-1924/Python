def verySlowFunction():
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    return 70

# # a = verySlowFunction()
if((a:=verySlowFunction())>10):
    print(a)

else:
    print("Its not greater than 10")

while(data:=input("Enter the value: ")):
    print(data)
    if data == "q":
        break

# The walrus operator is used to assign a value to a variable as part of an expression.
# This can be useful in situations where you want to use the value immediately after assigning it.
# For example, in the code above, the walrus operator is used to assign the result of the function verySlowFunction() to the variable a, and then check if a is greater than 10 in the same line.
# This can make the code more concise and easier to read, as it avoids the need for a separate assignment statement.