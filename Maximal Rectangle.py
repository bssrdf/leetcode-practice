class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        res = 0
        if matrix is None: return res
        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    print i, j
                    if j==0: dp[i][0] == 1
                    else: dp[i][j] = dp[i][j-1]+1
        print dp
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if dp[i][j]!=0:
                    k = i; width = dp[i][j]; height = 1
                    while k>=0:
                        width = min(width, dp[i][j])
                        area = width * height
                        res = max(res, area)
                        k-=1; height+=1
                        if dp[k][j] == 0: break
        return res

if __name__ == "__main__":
    s = Solution()
    matrix = [
        ["0","0","1","0"],
        ["1","1","1","1"],
        ["1","1","1","1"],
        ["1","1","1","0"],
        ["1","1","0","1"],
        ["1","1","1","1"],
        ["1","1","1","0"]
    ]
    print s.maximalRectangle(matrix)
    matrix = [
        ["1"]
    ]
    print s.maximalRectangle(matrix)