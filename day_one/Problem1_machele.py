"""
SUMMER OF '69: Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and extending to the next 9 
(every 6 will be followed by at least one 9).
"""


def summer_of69(array):
    if 6 in array and 9 in array:
        part_of_array_before_6 = array[ : array.index(6)]
        part_of_array_after_6 = array[array.index(6) : ]
        index_of_next_9 = part_of_array_after_6.index(9)

        result = sum(part_of_array_before_6 + part_of_array_after_6[index_of_next_9 + 1 : ])
    else:
        result = sum(array)

    return result


print(summer_of69([1, 3, 5]))
print(summer_of69([4, 5, 6, 7, 8, 9]))
print(summer_of69([2, 1, 6, 9, 11]))
print(summer_of69([2, 9, 6, 9, 11]))
