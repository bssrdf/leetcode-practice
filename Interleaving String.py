class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s3)!=len(s1)+len(s2): return False
        dp = [[False for j in range(len(s1)+1)] for i in range(len(s2)+1)]
        dp[0][0] = True
        for j in range(1, len(s1)+1):
            if s1[j-1] == s3[j-1]: dp[0][j] = True
        for i in range(1, len(s2)+1):
            if s2[i-1] == s3[i-1]: dp[i][0] = True
        for i in range(1, len(s2)+1):
            for j in range(1, len(s1)+1):
                if ((s3[i+j-1] == s1[j-1]) and dp[i][j-1]) or ((s3[i+j-1] == s2[i-1]) and dp[i-1][j]):
                    dp[i][j] = True
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    print s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    print s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    print s.isInterleave("", "abc", "abc")