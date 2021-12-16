import string
def isPanagram(str1, alphabet = string.ascii_lowercase):
	str1 = str1.lower()
	truth_list = []
	for i in alphabet:
		if i in "".join(str1):
			truth_list.append("true")

		else:
			truth_list.append("false")

	if "false" in truth_list:
		return False

	else:
		return True

# Test
print(isPanagram("The Quick brown fox jumps over The lazy dog"))
