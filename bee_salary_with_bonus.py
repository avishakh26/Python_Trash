name = str(input())

fixed_salary = float(input())

sales_total = float(input())


commission = sales_total * 0.15

final_salary = fixed_salary + commission


print(f"TOTAL = R$  {final_salary:.2F}")