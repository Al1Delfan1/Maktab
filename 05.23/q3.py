string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

new_string1 = string2[:2] + string1[2:]
new_string2 = string1[:2] + string2[2:]

result = new_string1 + ' ' + new_string2

print("Result:", result)
