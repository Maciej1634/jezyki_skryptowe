list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]
sorted_list = sorted(list_to_sort, key=lambda x: (x[1], x[2]))
print(sorted_list)
