def paper_doll(stringInput):
	stringInput = str(stringInput)
	new_chars = []
	for i in stringInput:
		i = i * 3
		new_chars.append(i)
	return "".join(new_chars)	

# Test 
print(paper_doll("hello"))