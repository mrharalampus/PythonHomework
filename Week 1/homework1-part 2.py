income = float(input("Enter yearly income: "))

if income < 10000:
    tax = income * 0.08
elif income <= 26000:
    tax = income * 0.12
else:
    tax = income * 0.24

print("Tax:", tax)