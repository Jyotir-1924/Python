flag = 'Y'
while(flag == 'Y'):
    try:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))

        print("Which operation you want to perform : \n\"+\" for Addition\n\"-\" for    Subtraction\n\"*\" for Multiplication\n\"/\" for Division")

        operation = input("Select the operation : ")
        match operation:
            case "+":
                print(f"The result is {num1 + num2}")
            case "-":
                print(f"The result is {num1 - num2}")
            case "*":
                print(f"The result is {num1 * num2}")
            case "/":
                print(f"The result is {num1 / num2}")
            case default:
                print("Invalid operation")
        
        flag = input("Continue ? (Y/N)\n")
        

    except Exception as e:
        print("Error Caused as : ",e)