import numpy as np

# Dictionary with the 90 degree turned version of applicable ascii characters
rot90 = {
    "/": "\\",
    "\\": "/",
    "-": "|",
    "|": "-",
}

# Dictionary with the 180 degree turned version of applicable ascii characters
rot180 = {
    "!": "¡", "!": "!",
    "&": "⅋", "⅋": "&",
    "(": ")", ")": "(",
    ",": "`", "`": ",",
    "'": ".", ".": "'",
    ";": "؛", "؛": ";",
    "<": ">", ">": "<",
    "?": "¿", "¿": "?",
    "[": "]", "]": "[",
    "^": "v", "v": "^",
    "{": "}", "}": "{",
}

# Converts a set of strings to a matrix of each individual character, based on a predefined matrix size
def to_matrix(pattern, size):
    matrix = np.chararray((int(size), int(size)),unicode=True)
    for index_r, row in enumerate(pattern):
        for index_c, column in enumerate(row):
            matrix[index_r][index_c] = column
    return matrix

# Changes characters in a matrix to their rotated versions by:
# Iterating through the matrix; testing each character to see if it is in a rotation dictionary; if it is, setting it to its rotated version
def rotate_characters(matrix, degrees):
    if degrees == 180:
        for object in matrix:
            return
    elif degrees == 90:
        for index_o, object in enumerate(matrix):
            for index_i, item in enumerate(object):
                if item in rot90:
                    matrix[index_o][index_i] = rot90.get(item)
        return matrix

# Needs to take a single matrix and a. rotate the ascii characters x degrees, b. rotate the matrix x degrees
# Potential input: Matrix, degrees of turn
def rotate(matrix, degrees):
    if degrees == 90:
        matrix = np.rot90(matrix)
    return matrix

# Needs to take a matrix, gather the necessary rotations of that matrix, put them together, and output the entire thing
# Potential input: Matrix, degrees of turn, number of times to tessellate
def tessellate():
    return

# Test function to gather input and put it through the other functions
def get_input(data, repeat):
    rotation, size, *pattern = data.split("\n")
    matrix = rotate(rotate_characters(to_matrix(pattern, size), 90), 90)
    print(pattern)
    print(matrix)

get_input("""90
4
####
#--#
#++#
####""", 1)
