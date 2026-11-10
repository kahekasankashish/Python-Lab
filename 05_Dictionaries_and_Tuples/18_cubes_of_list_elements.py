# Q18. Define a one-line procedure cubes(L) that returns a list containing the cube of each element of L.
def cubes(L):
    return [number ** 3 for number in L]

print(cubes([1, 2, 3]))
