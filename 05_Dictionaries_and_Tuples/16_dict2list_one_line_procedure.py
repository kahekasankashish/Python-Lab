# Q16. Define a one-line procedure dict2list(dct, keylist) that returns values in the order specified by keylist.
def dict2list(dct, keylist):
    return [dct[key] for key in keylist]

dct = {'a': 'A', 'b': 'B', 'c': 'C'}
keylist = ['b', 'c', 'a']
print(dict2list(dct, keylist))
