from operator import itemgetter

sample_list = [(2, 5), (1, 2), (4, 4)]

sorted_list = sorted(sample_list, key=itemgetter(-1))

print(sorted_list)
