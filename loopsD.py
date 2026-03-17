a,b,c,d = map(int,input().split())


sum4 = a+b-c
sum5 = a+b*c

sum6 = a-b*c
sum9 = a-b+c

sum7 = a*b+c
sum8 = a*b-c


if sum4 == d:
    print("YES")
elif sum5 == d:
    print("YES")
elif sum6 == d:
    print("YES")
elif sum7 == d:
    print("YES")
elif sum8== d:
    print("YES")
elif sum9 == d:
    print("YES")
    
else:
    print("NO")
    
    
    