nested_list = [[1, 2, 3], ['sam', 'kevin']]
final_list = [i for x in nested_list for i in x]
print(nested_list)