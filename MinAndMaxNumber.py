def min_No_in_list(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
    return min
print(min_No_in_list([3,8,15,2,7]))

def max_No_in_List(list):
    max = list[0]
    for a in list:
        if a>max:
            max = a
    return max
print(max_No_in_List([1,26,89,56,23]))