def tuple_to_dict(tup):
    result_dict = {}
    
    num_items = len(tup)
    
    if num_items % 2 != 0:
        num_items -= 1
    
    for i in range(0, num_items, 2):
        result_dict[tup[i]] = tup[i + 1]
    
    return result_dict

example_tuple = (2, "Python", (3, 5), [2, "Python", (3, 5)], "Maktab")
result_dict = tuple_to_dict(example_tuple)
print(result_dict)