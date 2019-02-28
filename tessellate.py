import numpy as np
import math

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
    matrix = np.chararray((size, size),unicode=True)
    for index_r, row in enumerate(pattern):
        for index_c, column in enumerate(row):
            matrix[index_r][index_c] = column
    return matrix

# Changes characters in a matrix to their rotated versions by:
# Iterating through the matrix; testing each character to see if it is in a rotation dictionary; if it is, setting it to its rotated version
def rotate_characters(matrix, degrees):
    if degrees % 360 != 0:
        if degrees % 180 == 0:
            for index_o, object in enumerate(matrix):
                for index_i, item in enumerate(object):
                    if item in rot180:
                        matrix[index_o][index_i] = rot180.get(item)
        elif degrees % 90 == 0:
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
    rotation = int(rotation)
    size = int(size)

    final_matrix = None

    # Each repeat will require a total of 4 matrixes to be combined, consisting of the original, two of the normal rotation, and one of the rotation * 2.
    # This loop should eventually make it possible to repeat this process as many times as desired with increasingly large matrices.
    # Currently, it only gathers the 3 unique necessary matrices for one repeat.
    for i in range(1, repeat+1):

        matrix_1 = to_matrix(pattern, size)
        matrix_2 = rotate(rotate_characters(to_matrix(pattern, size), rotation), rotation)
        matrix_3 = rotate(rotate_characters(to_matrix(pattern, size), rotation*2), rotation*2)
        top_matrix = np.hstack((matrix_1, matrix_2))
        bottom_matrix = np.hstack((matrix_2, matrix_3))
        final_matrix = np.vstack((top_matrix, bottom_matrix))

    # Takes the combined matrix (of four matrices * number of repeats) and prints it out as a string separated by new lines
    for item in final_matrix:
        stri = ''.join(str(r) for r in item)
        print(stri)

#Example command
# NOTE - Negative degrees are not currently functional
tessellate("""90
5
^^^^^
^|||^
^|||^
^|||^
^^^^^""", 1)
