class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0: return 0
        dp = [0 for i in range(len(s)+1)]
        dp[0]=1; 
        if s[0] >= '1' and s[0]<='9': dp[1]=1
        for i in range(2, len(dp)):
            if s[i-2:i] >='10' and s[i-2:i] <= '26':
                dp[i] += dp[i-2]
            if s[i-1] >= '1' and s[i-1] <= '9':
                dp[i] += dp[i-1]
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print s.numDecodings("011")
    print s.numDecodings("")
    print s.numDecodings("1")
    print s.numDecodings("10")
