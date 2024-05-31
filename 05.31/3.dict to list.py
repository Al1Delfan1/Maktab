mydict = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

unique_values = set()

for value in mydict.values():
    unique_values.add(value)

unique_values_list = list(unique_values)

print(unique_values_list)
