# write your code here
def blank_matrix():
    print("---------")
    for i in range(0, 3):
        print("| {} {} {} |".format(' ', ' ', ' '))
    print("---------")


# def input_grid():
#     user_input = input("> ")
#     first_row = user_input[:3]
#     second_row = user_input[3:6]
#     third_row = user_input[6:9]
#     matrix = [[s for s in first_row], [s for s in second_row], [s for s in third_row]]
#     return matrix

# print the grid
def print_grid(matrix):
    print("---------")
    for i in range(0, 3):
        print("| {} {} {} |".format(matrix[i][0], matrix[i][1], matrix[i][2]))
    print("---------")


# userInputIndex
def user_makeAMove():
    global player
    flag = True
    while flag:
        user_input = list(input("> ").split())
        if check_input_flag(user_input):
            moves = list(map(int, user_input))
            new_moves = []
            for m in moves:
                new_moves.append(int(m) - 1)
            if check_vacant_position(new_moves[0], new_moves[1]):
                matrix[new_moves[0]][new_moves[1]] = player
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
                flag = False
            else:
                print("This cell is occupied! Choose another one!")


# function to check all integer & not more than 4
def check_input_flag(user_input):
    flag = True
    if not all(ele.isdigit() for ele in user_input):
        print("You should enter numbers!")
        flag = False
    else:
        user_input = list(map(int, user_input))
        for ele in user_input:
            if ele > 3 or ele < 1:
                print("Coordinates should be from 1 to 3!")
                flag = False
                break
    return flag


def check_vacant_position(row, column):
    if matrix[row][column] == '_' or matrix[row][column] == ' ':
        return True
    else:
        return False


# checkImpossible function
# def checkImpossible(matrix):
#     isChecked = False
#     arrays = ([x for r in matrix for x in r])
#     if abs(arrays.count('X') - arrays.count('O')) > 1:
#         print("Impossible")
#         isChecked = True
#     if not isChecked:
#         if all(element == matrix[0][0] for element in matrix[0]) and (
#                 all(element == matrix[1][0] for element in matrix[1]) or all(
#             element == matrix[2][0] for element in matrix[2])):
#             print("Impossible")
#             isChecked = True
#         elif all(element == matrix[1][0] for element in matrix[1]) and all(
#                 element == matrix[2][0] for element in matrix[2]):
#             print("Impossible")
#             isChecked = True
#         if not isChecked:
#             if (matrix[0][0] == matrix[1][0] == matrix[2][0]) and (
#                     matrix[0][1] == matrix[1][1] == matrix[2][1] or matrix[0][2] == matrix[1][2] == matrix[2][2]):
#                 print("Impossible")
#                 isChecked = True
#     return isChecked


def analyse_game(matrix):
    # isChecked = checkImpossible(matrix)
    # isChecked = False
    global isGameFinished
    # if not isChecked:
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != ' ':
        print("{} wins".format(matrix[0][0]))
        isGameFinished = True
    elif matrix[2][0] == matrix[1][1] == matrix[0][2] != ' ':
        print("{} wins".format(matrix[2][0]))
        isGameFinished = True
    else:
        for i in range(0, 3):
            if matrix[i][0] == matrix[i][1] == matrix[i][2] != ' ':
                print("{} wins".format(matrix[i][0]))
                isGameFinished = True
            elif matrix[0][i] == matrix[1][i] == matrix[2][i] != ' ':
                print("{} wins".format(matrix[0][i]))
                isGameFinished = True


# main
global matrix
player = 'X'
isGameFinished = False
matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
blank_matrix()
counter = 0
while not isGameFinished and counter <= 9:
    counter += 1
    if counter > 9:
        print("Draw")
        isGameFinished = True
    else:
        user_makeAMove()
        print_grid(matrix)
        analyse_game(matrix)
