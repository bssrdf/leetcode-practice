class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1: return 1
        if n == 2: return 2
        dp = [0 for i in range(n)]
        dp[0]=1; dp[1]=2
        for i in range(2, n):
            dp[i] = dp[i-2]+dp[i-1]
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print s.climbStairs(3)
    print s.climbStairs(4)