# Q13. Create a list containing five numbers. Create another list which contains the cube of the numbers of the first list using map().
numbers = []
for index in range(5):
    numbers.append(float(input(f"Enter number {index + 1}: ")))

cubes = list(map(lambda number: number ** 3, numbers))
print("Original list:", numbers)
print("Cubes:", cubes)
