#it is nested list : a list contain another list . operation have working of make  single list 
# flattened = []

# for sublist in nested_list:
#     for item in sublist:
#         flattened.append(item)
nested_list = [[1, 2, 3], [4, 5], [6]]
flattened = [item for sublist in nested_list for item in sublist]