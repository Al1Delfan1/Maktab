num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

multiplied = num1 * num2

if multiplied <= 1000:
    result = multiplied
else:
    result = num1 + num2

print("Result:", result)
