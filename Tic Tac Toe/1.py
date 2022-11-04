from random import randrange

# i = 0
# row = 0
# board = [1, 2, 3, 4, "x", 6, 7, 8, 9]


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    wall = ("+" + "-" * 7) * 3 + "+"
    for column in board:
        print(wall)
        for row in column:
            print(f"|\t{row}", end="\t")
        print('|')

        print("\n", end="")
    print(wall)


def check_move(board, option):
    while True:
        while option < 0 or option > 10:
            print("Wrong option choose again")
            option = int(input('your option '))

        for column in board:
            for row in column:
                if row == option:
                    return True
        return False


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    users_option = int(input('your option '))
    column = 0
    while not check_move(board=board, option=users_option):
        check_move(board=board, option=users_option)
        users_option = int(input('it is occupied, try again '))
    while column < 3:
        for row in range(0, 3):
            if board[column][row] == users_option:
                board[column][row] = 'O'
        column += 1


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    column, row = 0, 0
    while row < 3:
        if board[column][row] == board[column + 1][row] == board[column + 2][row]:
            return sign == board[column][row]
        row += 1
    column, row = 0, 0
    while column < 3:
        if board[column][row] == board[column][row + 1] == board[column][row + 2]:
            return sign == board[column][row]
        column += 1
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return sign == board[1][1]


def draw(board):
    count = 0
    for column in board:
        for row in column:
            if type(row) is not int:
                count += 1
    if count == 9:
        return "D"


def draw_move(board):
    # The function draws the computer's move and updates the board.
    column = 0
    computers_option = randrange(1, 10)
    while check_move(board=board, option=computers_option) == False:
        check_move(board=board, option=computers_option)
        computers_option = randrange(1, 10)
    while column < 3:
        for row in range(0, 3):
            if board[column][row] == computers_option:
                board[column][row] = 'X'
        column += 1


# while i < 10 and row < 9:
#     if row != 1  and  row != 4 and  row != 7:
#         print('|       ' * 3, '|')
#
#     else:
#         print('|  ', board[i], ' ', '|  ', board[i + 1], ' ', '|  ', board[i + 2], '   |')
#         i += 3
#     if row == 2 or row == 5 or row == 8:
#         print('+-------' * 3, '+')
#
#     row += 1

def main():
    matrix = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

    while True:
        display_board(board=matrix)
        enter_move(board=matrix)
        if victory_for(board=matrix, sign='O') == True:
            display_board(board=matrix)
            print('You are winner')
            break
        if draw(board=matrix) == "D":
            print('Draw')
            break

        draw_move(board=matrix)
        if victory_for(board=matrix, sign='X') == True:
            display_board(board=matrix)
            print('Looser')
            break
        if draw(board=matrix) == "D":
            print('Draw')
            break
main()
