def spy_game(nums):
    check = []
    for i in nums:
        if i == 0:
            check.append(0)
        elif i == 7:
            check.append(7)
    # if check == [0,0,7]:
    #     return True
    for i in range(len(check)+1):
        if check[i:i+3] == [0,0,7]:
            return True
    return False
   

print(spy_game([1,2,4,0,0,7,5]))
print( spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
print(spy_game([1,7,2,0,4,5,0,7]))