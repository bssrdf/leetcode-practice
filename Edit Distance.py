class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        dp = [[0 for j in range(len(word1)+1)] for i in range(len(word2)+1)]
        for j in range(len(word1)+1):
            dp[0][j] = j
        for i in range(len(word2)+1):
            dp[i][0] = i
        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word2[i-1] == word1[j-1]: 
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1]+1, dp[i-1][j]+1)
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i][j-1]+1, dp[i-1][j]+1)
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    print s.minDistance("cat", "dag")