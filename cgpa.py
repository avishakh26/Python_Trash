
name =  str(input("Enter your Name :"))
semester = (input ("Enter your Semester : "))
id = int(input("Enter your student ID : "))
section = int(input("Which section you are in: "))
cr = str (input("Enter your CR Name : "))




a = int(input("Enter your DIC number : "))
b = int(input("Enter your DM number : "))
c = int(input("Enter your CAFA number : "))
d = int(input("Enter your EEE number : "))
e = int(input("Enter your PHYSICS number : "))

avg = (a+b+c+d+e)/5

if avg>=40 and avg<60:
    print("You are passed ")
    
    
elif avg<40:
    print("You are fail")
    
elif avg >= 80:
    print("Congratulation your CG is 4.00")
 
elif avg >=75: 
    print("Your CG is 3.75")
    
elif avg>=70:
    print("Your CG is 3.50")  
    
elif avg>=60:
    print("Your CG is 3.00 ")
    
    
else :
    print("Your input number is wrong. Please input another number.")