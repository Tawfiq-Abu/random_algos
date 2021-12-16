def paper_doll(word):
    triple = [w*3 for w in word]
    triple = ''.join(triple)
    return triple

print(paper_doll("how"))
print(paper_doll("signal"))
print(paper_doll("mcsam"))
