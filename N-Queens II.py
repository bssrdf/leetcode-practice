class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.res = 0
        self.totalNQueensRecur([], n)
        return self.res

    def totalNQueensRecur(self, cur, n):
        if len(cur) == n:
            self.res += 1
        for i in range(n):
            if i not in cur and reduce(lambda x, y: x and abs(i-cur[y])!=abs(len(cur)-y),range(len(cur)), True):
                self.totalNQueensRecur(cur+[i], n)

if __name__ == "__main__":
    s = Solution()
    print s.totalNQueens(4)   

