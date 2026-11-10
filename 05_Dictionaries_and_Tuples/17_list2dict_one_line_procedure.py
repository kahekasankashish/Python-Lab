# Q17. Define a one-line procedure list2dict(L, keylist) mapping keylist[i] to L[i].
def list2dict(L, keylist):
    return {key: value for value, key in zip(L, keylist)}

L = ['A', 'B', 'C']
keylist = ['a', 'b', 'c']
print(list2dict(L, keylist))
