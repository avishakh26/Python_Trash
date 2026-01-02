year = int(input("Enter your year :"))

if year %4 == 0:
    print("Yes it's a leap year")
    
    
elif year %100==0 and year %400==0:
    print("Yes it's a leap year")
    
    
else:
    print("No , It's not a leap year")