class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.solveSudokuRecur(board)

    def solveSudokuRecur(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    for k in "123456789":
                        if self.isValid(board, i, j, k):
                            board[i][j] = k
                            if self.solveSudokuRecur(board):
                                return True
                            else: board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, i, j, val):
        for ii in range(9):
            if board[i][ii] == val: return False
        for jj in range(9):
                if board[jj][j] == val: return False
        for ii in range(3):
            for jj in range(3):
                if board[i/3*3+ii][j/3*3+jj] == val: return False
        return True

if __name__ == "__main__":
    s = Solution()
    a = [['5','3','.','.','7','.','.','.','.'],
         ['6','.','.','1','9','5','.','.','.'],
         ['.','9','8','.','.','.','.','6','.'],
         ['8','.','.','.','6','.','.','.','3'],
         ['4','.','.','8','.','3','.','.','1'],
         ['7','.','.','.','2','.','.','.','6'],
         ['.','6','.','.','.','.','2','8','.'],
         ['.','.','.','4','1','9','.','.','5'],
         ['.','.','.','.','8','.','.','7','9']]
    for i in a:
        print i
    print "\n"
    s.solveSudoku(a)
    for i in a:
        print i  
