# Module containing basic matrix operations.
def _validate_rectangular(matrix):
    if not matrix or not matrix[0]:
        raise ValueError("Matrix must not be empty")
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("Matrix rows must all have the same length")

def add_matrices(first, second):
    _validate_rectangular(first)
    _validate_rectangular(second)
    if len(first) != len(second) or len(first[0]) != len(second[0]):
        raise ValueError("Matrices must have the same dimensions for addition")
    return [
        [first[row][column] + second[row][column] for column in range(len(first[0]))]
        for row in range(len(first))
    ]

def transpose(matrix):
    _validate_rectangular(matrix)
    return [list(row) for row in zip(*matrix)]
