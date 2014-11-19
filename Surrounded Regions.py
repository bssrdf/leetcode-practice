class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    # def solve(self, board):
    #     if board == []: return []
    #     for i in range(len(board)):
    #         self.search(board, i, 0)
    #         self.search(board, i, len(board[0])-1)
    #     for i in range(len(board[0])):
    #         self.search(board, 0, i)
    #         self.search(board, len(board)-1, i)
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if board[i][j] == 'O':
    #                 board[i][j] = 'X'
    #             if board[i][j] == 'P':
    #                 board[i][j] = 'O' 

    # def search(self, board, i, j):
    #     if i<0 or i>len(board)-1: return
    #     if j<0 or j>len(board[0])-1: return
    #     if board[i][j] == 'O':
    #         board[i][j] = 'P'
    #         self.search(board, i+1, j)
    #         self.search(board, i-1, j)
    #         self.search(board, i, j+1)
    #         self.search(board, i, j-1)
    def solve(self, board):
        if board == []: return
        queue = []; 
        for i in range(len(board)):
            if board[i][0] == 'O': queue.append((i, 0))
            if board[i][len(board[0])-1] == 'O': queue.append((i, len(board[0])-1))
        for i in range(len(board[0])):
            if board[0][i] == 'O': queue.append((0, i))
            if board[len(board)-1][i] == 'O': queue.append((len(board)-1, i))
        while queue:
            t = queue.pop(0)
            row = t[0]; col = t[1]
            if board[row][col] == 'O':
                board[row][col] = 'P'
                if row+1<=len(board)-1: queue.append((row+1, col))
                if row-1>=0: queue.append((row-1, col))
                if col+1<=len(board[0])-1: queue.append((row, col+1))
                if col-1>=0: queue.append((row, col-1))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'P':
                    board[i][j] = 'O' 

if __name__ == "__main__":
    s = Solution()
    input = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"]
    ]
    for i in input: print i
    print "\n"
    s.solve(input)
    for i in input: print i
    print "\n"
