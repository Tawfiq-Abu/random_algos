"""
Trust me, this isn't the best solution
It might still work in cases where the numbers aren't in order.
"""

def spy_game(int_array):
    try:
        index_of_first_0 = int_array.index(0)
        int_array.pop(index_of_first_0)
        index_of_next_0 = int_array.index(0)
        int_array.pop(index_of_next_0)
        index_of_7 = int_array.index(7)
        int_array.pop(index_of_7)

        return True

    except:
        return False

print(spy_game([1,2,9,0,2,0,7]))
print(spy_game([1,2,9,0,2,7,0]))
print(spy_game([1,2,9,0,2,7,0, 0, 7]))
