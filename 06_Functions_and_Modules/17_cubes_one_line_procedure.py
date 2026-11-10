# Q17. Define a one-line procedure cubes(L): input is a list L of numbers; output is a list whose ith element is the cube of the ith element of L.
def cubes(L): return [number ** 3 for number in L]

print(cubes([1, 2, 3]))
