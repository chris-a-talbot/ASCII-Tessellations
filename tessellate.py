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
        for index_o, object in enumerate(matrix):
            for index_i, item in enumerate(object):
                if item in rot180:
                    matrix[index_o][index_i] = rot180.get(item)
    elif degrees == 90:
        for index_o, object in enumerate(matrix):
            for index_i, item in enumerate(object):
                if item in rot90:
                    matrix[index_o][index_i] = rot90.get(item)
    return matrix

# Takes a matrix (in this case, a numpy chararray and rotates it given degrees)
# Numpy rot90 function rotates an array 90 degrees, but it seems the original post wants a -90 degree turn; because of this, I set a 90 degree turn to actually turn 270 degrees.
# If degrees are not a valid option or do not need any change (0 degrees), matrix returns as it came in
def rotate(matrix, degrees):
    if degrees == 90:
        matrix = np.rot90(matrix, 3)
    elif degrees == 180:
        matrix = np.rot90(matrix, 2)
    elif degrees == 270 or degrees == -90:
        matrix = np.rot90(matrix)
    return matrix

# Needs to take a matrix, rotate the matrix as much as necessary, put all of the necessary matrixes together, and output it as a set of strings
# Takes user input. Data variable takes: Rotation in degrees, size of the square matrix, and the pattern of the matrix. Repeat takes the number of times to repeat the process.
# This part is a WIP.
def tessellate(data, repeat):
    rotation, size, *pattern = data.split("\n")
    matrix = rotate(rotate_characters(to_matrix(pattern, size), 90), 90)
    return

tessellate("""90
4
####
#--#
#++#
####""", 1)
