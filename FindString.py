
def find_str(matrix, val, los):
    for string in los:
        is_present = is_string_present_in_matrix_pre(matrix, val, string)
        if is_present:
            print(string + " is present ")
        else:
            print(string + " is not present")


def is_string_present_in_matrix_pre(matrix, val, string):
    for i in range(val):
        for j in range(val):
            if matrix[i][j] == string[0]:
                return is_string_present_in_matrix(matrix, val, string, i, j, [])
    return False


def is_string_present_in_matrix(matrix, val, string, row, col, visited_locs):
    if string == '':
        return True
    if (row, col) in visited_locs:
        return False
    if row < 0 or row >= val or col < 0 or col >= val:
        return False

    if matrix[row][col] == string[0]:
        string = string[1:]
        visited_locs.append((row, col))

        # traverse all the nearest neighbours
        results = []
        results.append(is_string_present_in_matrix(matrix, val, string, row + 1, col, visited_locs))
        results.append(is_string_present_in_matrix(matrix, val, string, row - 1, col, visited_locs))
        results.append(is_string_present_in_matrix(matrix, val, string, row + 1, col + 1, visited_locs))
        results.append(is_string_present_in_matrix(matrix, val, string, row - 1, col + 1, visited_locs))
        results.append(is_string_present_in_matrix(matrix, val, string, row + 1, col - 1, visited_locs))
        results.append(is_string_present_in_matrix(matrix, val, string, row - 1, col - 1, visited_locs))
        results.append(is_string_present_in_matrix(matrix, val, string, row, col + 1, visited_locs))
        results.append(is_string_present_in_matrix(matrix, val, string, row, col - 1, visited_locs))
        visited_locs.remove((row, col))
        return any(results)
    else:
        return False


if __name__ == '__main__':
    #matrix = list()
    los = ['abc', 'def', 'abe', 'abf', 'aba', 'abehg', 'efcba', 'efcb', 'abi', 'aei']
    # val = int(input("Enter value of n for N X N Matrix: "))
    # for i in range(val):
    #     row = list()
    #     for j in range(val):
    #         row.append(str(input("Enter value of grid [" + str(i) + "] [" + str(j) + "]")))
    #     matrix.append(row)
    val = 3
    matrix = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    find_str(matrix, val, los)
