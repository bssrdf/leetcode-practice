class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid); n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==1: break
            else: dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j]==1: break
            else: dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]==1: dp[i][j]=0
                else: dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

if __name__ == "__main__":
    s = Solution()
    print s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) 
