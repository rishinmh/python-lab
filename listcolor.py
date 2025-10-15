color_list1 = input("enter color for list1: ").split()
color_list2 = input("enter color for list2: ").split()
set1 = set(color_list1)
set2 = set(color_list2)
result = set1 - set2
print("result: ", result)
