class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        res = False
        visited = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = res or self.existRecur(board, word, i, j, visited)
        return res
        
    def existRecur(self, board, word, i, j, visited):
        if word is '': return True
        if i<0 or i>=len(board): return False
        if j<0 or j>=len(board[0]): return False
        char = word[0]
        if char == board[i][j] and visited[i][j]==0: 
            visited[i][j]=1
            if (self.existRecur(board, word[1:],i-1,j, visited) or self.existRecur(board, word[1:],i+1,j, visited) or self.existRecur(board, word[1:],i,j-1, visited) or self.existRecur(board, word[1:],i,j+1, visited)) is False:
                visited[i][j]=0; return False
            else: return True
        return False

if __name__ == "__main__":
    s = Solution()
    b = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    print s.exist(b, "ABCCED")
    print s.exist(b, "SEE")
    print s.exist(b, "ABCB")
    b = [["a", "a"]]
    print s.exist(b, "aa")
    b = [["a"]]
    print s.exist(b, "a")