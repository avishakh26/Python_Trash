
print('''=== --- Welcome to my simple calculator --- ===
      
        1. Addition
        2. Division
        3. Multiplication
        4. Substraction
      
      ''')


user_Redirect_Input = int(input("Enter Your Choose : ")) 

if(user_Redirect_Input == 1):

    numberOne = int(input("Input For Number One : "))
    numberTwo = int(input("Input For Number Two : "))
    answer = numberOne + numberTwo
    print(f"Your Answer is : {answer}")

elif(user_Redirect_Input == 2):

    numberOne = int(input("Input For Number One : "))
    numberTwo = int(input("Input For Number Two : "))
    answer = numberOne - numberTwo
    print("Your Answer is : " , answer)

elif(user_Redirect_Input == 3):

    numberOne = int(input("Input For Number One : "))
    numberTwo = int(input("Input For Number Two : "))
    answer = numberOne * numberTwo
    print("Your Answer is : " , answer)

elif(user_Redirect_Input == 4):

    numberOne = int(input("Input For Number One : "))
    numberTwo = int(input("Input For Number Two : "))
    answer = numberOne / numberTwo
    print("Your Answer is : " , answer)

else:
    print("Your Input Is Wrong Please Try Again")