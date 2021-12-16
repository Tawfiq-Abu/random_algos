def summer_69(arrayList):
	import array
	if 6 not in arrayList or 9 not in arrayList: 
		arrayTotal = 0 
		for i in range(0, len(arrayList)):
			arrayTotal = arrayTotal + arrayList[i]

		return arrayTotal

	elif 6 in arrayList and 9 in arrayList:
		new_array = array.array('i',[])
		for i in arrayList:
			if arrayList.index(i) <arrayList.index(6) or arrayList.index(i)>arrayList.index(9):
				new_array.append(i)

		total = 0
		for i in range(0, len(new_array)):
			total = total + new_array[i]

		return total

# Tests
print(summer_69([1,3,5])) # 1

print(summer_69([4,5,6,7,8,9])) # 2

print(summer_69([2,1,6,9,11])) # 3