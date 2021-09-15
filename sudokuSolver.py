import running
import random


def printBoard(board):

    for i in range(len(board)):
        if i % 3 == 0:
            print('- - - - - - - - - - - - -')

        for j in range(len(board[i])):
            if j % 3 == 0:
                print('| ' + str(board[i][j]) + ' ', end='')

            elif j == 8:
                print(str(board[i][j]) + ' |')

            else:
                print(str(board[i][j]) + ' ', end='')

        if i == 8:
            print('- - - - - - - - - - - - -')


def ifEmpty(board):  # an empty is needed to solve and apply algorithims

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0:
                    return i, j

        return None


def validNumReplacement(board, num, position_cell):

        # Check if num exists in Row, sudoku rules
        for i in range(len(board[position_cell[0]])):
            if board[position_cell[0]][i] == num and position_cell[1] != i:
                return False

        # Check if num exists in Column, sudoku rules
        for j in range(len(board[position_cell[1]])):
            if board[j][position_cell[1]] == num and position_cell[0] != j:
                return False

        # Checking num in the box, sudoku rules
        box_row = position_cell[0] // 3
        box_col = position_cell[1] // 3

        for i in range(box_row*3, box_row*3 + 3):
            for j in range(box_col*3, box_col*3 + 3):
                if board[i][j] == num and (i, j) != position_cell:
                    return False
                    

def solveSudoku(board):
        find = ifEmpty(board)

        if not find:
            return True
        else:
            position = find

        for tryNum in range(1, 10):
            if validNumReplacement(board, tryNum, position):
                board[position[0]][position[1]] = tryNum

                if solveSudoku():
                    return True

                board[position[0]][position[1]] = 0

        return False


if __name__ == '__main__':

    gameBoard = random.choice(running.boards)
    printBoard(gameBoard)
    solveSudoku(gameBoard)
    print("<<<<<<<<--Board-solved-->>>>>>")
    printBoard(gameBoard)
