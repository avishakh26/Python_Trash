terminate = False

while not terminate:
    num1 = int(input("Please enter a number : "))
    num2 = int(input("Please enter another number : "))
    
    while True:
        operation = input("Please enter 'add/sub' or 'quit' to exit :")
        
        if operation == "quit":
            termintate = True
            
            break
        
        if operation not in ["add","sub"]:
            print("Unknown operation!")
            
            continue
        
        
        if operation == "add":
            print("Result is ",num1+num2)
            
            break
        
        if operation == "sub":
            print("Result is ",num1-num2)
            
            break
        