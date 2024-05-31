a = int(input('enter start number: '))
b = int(input('enter end number: '))

prime_numbers = []

for numbers in range(a, b):
    count = True
    for i in range(2, numbers):
        if numbers % i == 0:
            count = False
    if count:
        prime_numbers.append(numbers)

print(prime_numbers)