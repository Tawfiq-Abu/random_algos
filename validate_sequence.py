def validate_subsequence(arr1,arr2):
    c=[]
    j = arr2.copy()
    for i in arr1:
        if i == arr2[0]:
            c.append(arr2[0])
            arr2.pop(0)
    return c == j
    

print(validate_subsequence([1,2,3,4,5],[2,3,5]))
print(validate_subsequence([1,2,3,4],[1,3,4]))