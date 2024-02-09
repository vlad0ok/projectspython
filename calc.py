num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation(+, -, * or /: ")
result = 0
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 // num2

print(f"Your answer is {result}")