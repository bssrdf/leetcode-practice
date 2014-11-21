class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        res = []
        self.solveNQueensRecur(res, [], n)
        return res

    def solveNQueensRecur(self, res, cur, n):
        if len(cur) == n:
            board = []
            for i in cur:
                board.append("."*i+"Q"+"."*(n-i-1))
            res.append(board)
        for i in range(n):
            # not same column & not diagonal
            if i not in cur and reduce(lambda x, y: x and (abs(y-len(cur))!=abs(cur[y]-i)), range(len(cur)), True):
                self.solveNQueensRecur(res, cur+[i], n)

if __name__ == "__main__":
    s = Solution()
    print s.solveNQueens(4)
