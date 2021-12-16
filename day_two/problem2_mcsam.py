def spy_game(arrayInput):
  new_array = []
  for i in arrayInput:
    if i == 0 or i == 7:
      print(i)
      new_array.append(i)
    else:
      pass
  if new_array == [0,0,7]:
    return True
  else:
    return False

# Tests
print(spy_game([1,2,4,0,0,7,5])) # Test 1
print(spy_game([1,0,2,4,0,5,7])) # Test 2
print(spy_game([1,7,2,0,4,5,0])) # Test 3