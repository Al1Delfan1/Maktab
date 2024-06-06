def count_upper_lower(s):
    upper_count = 0
    lower_count = 0
    
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    print("No. of Lower case characters:", lower_count)
    print("No. of Upper case characters:", upper_count)

input_string = "The quick Brow Fox"

count_upper_lower(input_string)