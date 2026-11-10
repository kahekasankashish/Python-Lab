"""
Question: Write a program that will display the six patterns shown in Assignment 3: Half Pyramid, Inverted Half Pyramid, Hollow Inverted Half Pyramid, Full Pyramid, Inverted Full Pyramid, and Hollow Full Pyramid.
"""

rows = int(input("Enter number of rows: "))

if rows <= 0:
    print("Number of rows must be positive.")
else:
    print("\n1. Half Pyramid")
    for i in range(1, rows + 1):
        print("* " * i)

    print("\n2. Inverted Half Pyramid")
    for i in range(rows, 0, -1):
        print("* " * i)

    print("\n3. Hollow Inverted Half Pyramid")
    for i in range(rows, 0, -1):
        if i == rows or i == 1:
            print("* " * i)
        else:
            print("* " + "  " * (i - 2) + "* ")

    print("\n4. Full Pyramid")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

    print("\n5. Inverted Full Pyramid")
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "* " * i)

    print("\n6. Hollow Full Pyramid")
    for i in range(1, rows + 1):
        if i == 1:
            print(" " * (rows - 1) + "*")
        elif i == rows:
            print("* " * rows)
        else:
            print(" " * (rows - i) + "*" + " " * (2 * i - 3) + "*")
