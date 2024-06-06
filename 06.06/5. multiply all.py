from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

numbers = [8, 2, 3, -1, 7]

output = multiply_list(numbers)
print(output)
