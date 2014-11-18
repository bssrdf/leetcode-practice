class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # check rows
        for i in range(9):
            check = [False for k in range(9)]
            for j in range(9):
                if board[i][j]!='.':
                    if check[int(board[i][j])-1]==True:
                        return False
                    else:
                        check[int(board[i][j])-1]=True
        # check columns
        for j in range(9):
            check = [False for k in range(9)]
            for i in range(9):
                if board[i][j]!='.':
                    if check[int(board[i][j])-1]==True:
                        return False
                    else:
                        check[int(board[i][j])-1]=True
        # check squares
        for i in range(3):
            for j in range(3):
                check = [False for k in range(9)]
                for row in range(3):
                    for col in range(3):
                        if board[i*3+row][j*3+col]!='.':
                            if check[int(board[i*3+row][j*3+col])-1]==True:
                                return False
                            else:
                                check[int(board[i*3+row][j*3+col])-1] = True
        return True

if __name__ == "__main__":
    s = Solution()
    a = [[5,3,'.','.',7,'.','.','.','.'],
         [6,'.','.',1,9,5,'.','.','.'],
         ['.',9,8,'.','.','.','.',6,'.'],
         [8,'.','.','.',6,'.','.','.',3],
         [4,'.','.',8,'.',3,'.','.',1],
         [7,'.','.','.',2,'.','.','.',6],
         ['.',6,'.','.','.','.',2,8,'.'],
         ['.','.','.',4,1,9,'.','.',5],
         ['.','.','.','.',8,'.','.',7,9]]
    print s.isValidSudoku(a)
    b = [['5', '3', '1', '2', '7', '6', '4', '9', '8'],
         ['6', '2', '3', '1', '9', '5', '8', '4', '7'],
         ['1', '9', '8', '3', '4', '7', '5', '6', '2'],
         ['8', '1', '2', '7', '6', '4', '9', '5', '3'],
         ['4', '7', '9', '8', '5', '3', '6', '2', '1'],
         ['7', '4', '5', '9', '2', '8', '3', '1', '6'],
         ['9', '6', '7', '5', '3', '1', '2', '8', '4'],
         ['2', '8', '6', '4', '1', '9', '7', '3', '5'],
         ['3', '5', '4', '6', '8', '2', '1', '7', '9']]
    print s.isValidSudoku(b)