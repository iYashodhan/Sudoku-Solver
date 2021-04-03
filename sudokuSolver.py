import random
import running


class Sudoku:

    def __init__(self):
        self.board = random.choice(running.boards)

    def printBoard(self):

        for i in range(len(self.board)):
            if i % 3 == 0:
                print('- - - - - - - - - - - - -')

            for j in range(len(self.board[i])):
                if j % 3 == 0:
                    print('| ' + str(self.board[i][j]) + ' ', end='')

                elif j == 8:
                    print(str(self.board[i][j]) + ' |')

                else:
                    print(str(self.board[i][j]) + ' ', end='')

            if i == 8:
                print('- - - - - - - - - - - - -')

    def ifEmpty(self):  # returns the position of an empty cell

        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    return i, j

        return None

    def validNumReplacement(self, num, position_cell):

        # Check if num exists in Row
        for i in range(len(self.board[position_cell[0]])):
            if self.board[position_cell[0]][i] == num and position_cell[1] != i:
                return False

        # Check if num exists in Column
        for j in range(len(self.board[position_cell[1]])):
            if self.board[j][position_cell[1]] == num and position_cell[0] != j:
                return False

        # Checking num in the box
        box_row = position_cell[0] // 3
        box_col = position_cell[1] // 3

        for i in range(box_row*3, box_row*3 + 3):
            for j in range(box_col*3, box_col*3 + 3):
                if self.board[i][j] == num and (i, j) != position_cell:
                    return False

        return True

    def solveSudoku(self):
        find = self.ifEmpty()

        if not find:
            return True
        else:
            position = find

        for tryNum in range(1, 10):
            if self.validNumReplacement(tryNum, position):
                self.board[position[0]][position[1]] = tryNum

                if self.solveSudoku():
                    return True

                self.board[position[0]][position[1]] = 0

        return False


if __name__ == '__main__':

    game = Sudoku()
    game.printBoard()
    game.solveSudoku()
    print("<<<<<<<<--Board-solved-->>>>>>")
    game.printBoard()
