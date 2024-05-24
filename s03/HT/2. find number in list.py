my_list = []
number = True
while number:
    number = input('n for break: ')
    if number == 'n':
        number = False
    else:
        my_list.append(int(number))


for item in my_list:
    if item <= 150 and item % 5 == 0:
        print(item)
    elif item > 500:
        break