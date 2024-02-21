num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Input Operator ")

if op == '+':
    print(f"{num1} + {num2} =", num1 + num2)
elif op == '-':
    print(f"{num1} - {num2} =", num1 - num2)
elif op == '*':
    print(f"{num1} * {num2} =", num1 * num2)
elif op == '/':
    print(f"{num1} / {num2}=", num1 / num2)
else:
    print('''
    Invalid oprator!
    Enter Valid operator
    ''')
