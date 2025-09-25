try:
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    
    print("What kind of operation do you want to perform .\npress + for addition\npress - for subtruction\npress * for multiplication\npress / for division ")
    
    o = input("Enter the operation:")
    match o:
        case "+":
            print(f"The result is:{a + b}")
        case "-":
            print(f"The result is:{a - b}")
        case "*":
            print(f"The result is:{a * b}")
        case "/":
            print(f"The result is:{a / b}")
        case default:
            print("There was a error ")    
    
except Exception as e:
    print("Enter the valid value of a and b")    
        