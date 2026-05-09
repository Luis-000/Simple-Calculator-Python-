#Calculator Exercise

operator = input ("Enter an operator (+ - * /): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")
elif operator == "-":
    total = num1 - num2
    print(f"{num1} - {num2} = {total}")
elif operator == "*":
    total = num1 * num2
    print(f"{num1} * {num2} = {round(total, 2)}")
elif operator == "/":
    total = num1 / num2
    print(f"{num1} / {num2} = {round(total, 2)}")
else:
    print(f"{operator} is not a Valid Operator!")