class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i-1]+grid[0][i]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[len(grid)-1][len(grid[0])-1]

if __name__ == "__main__":
    s = Solution()
    grid = [[1,2],[1,1]]
    print s.minPathSum(grid)
    print grid

