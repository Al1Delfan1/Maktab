input_string = input("Enter a string: ")

letter_count = 0
digit_count = 0

for char in input_string:
    if char.isalpha():  
        letter_count += 1
    elif char.isdigit():  
        digit_count += 1

print(f"Letters: {letter_count}")
print(f"Digits: {digit_count}")
