import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str2 = ''.join(str1)
    alpha = list(alphabet)
    alpha = alpha.sort()
    str3 = list(str2)
    str3 = str3.sort()
    if alpha == str3:
        return True
    return False

ispangram("The quick brown fox jumps over the lazy dog")