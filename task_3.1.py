inp = int(input("Enter your number : "))

if inp <= 16:
    
    for i in range(1,inp+1):
        if i % 2 == 0:
            print(i, end = " ")
            
            
else:
    print("Input is wrong")
    
    
    
    