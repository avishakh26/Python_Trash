li = [1,2,3,4]
new_li = []

for x in li:
    new_li.append(x*2)
    
print(new_li)

new_li = [2 * x for x in li]
print(new_li)






even_numbers =[x for x in range(1,11) if x %2==0]
print(even_numbers)                                     #by using list comprehensions








                #81 page challanges :



numbers = [1, 2, 3, 4, 5]


squares = [x ** 2 for x in numbers]


print(squares)

