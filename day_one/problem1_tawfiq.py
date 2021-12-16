def summer_69(arr):
    l = []
    g = []
    s = []
    count = 0
    for index,val in enumerate(arr):
        if val == 6:
            l = arr[:index]
        elif val == 9:
            g= arr[index+1:]
    s = l+g
    if len(s) == 0 and 6 not in arr:
        return sum(arr)
    return sum(s)
    
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))