marks = input ("Enter your marks :")
marks = int (marks)

if marks>= 80:
    grade = "A+"
elif marks >=70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"

else:
    grade = "F"

print("Your result is ", grade ," grade")