class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        dp = [[0 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]
        dp[-1][-1] = max(1-dungeon[-1][-1], 1)
        for i in reversed(range(len(dungeon)-1)):
            dp[i][-1] = max(dp[i+1][-1]-dungeon[i][-1], 1)
        for j in reversed(range(len(dungeon[0])-1)):
            dp[-1][j] = max(dp[-1][j+1]-dungeon[-1][j], 1)
        for i in reversed(range(len(dungeon)-1)):
            for j in reversed(range(len(dungeon[0])-1)):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1])-dungeon[i][j], 1)
        return dp[0][0]

if __name__ == "__main__":
    s = Solution()
    dungeon = [[-2,-3,3],
               [-5,-10,1],
               [10,30,-5]]
    print s.calculateMinimumHP(dungeon)
