class Solution:
    # @return a boolean
    # def isScramble(self, s1, s2):
    #     if s1 == s2: return True
    #     if len(s1) != len(s2): return False
    #     for i in range(1, len(s1)):
    #         if self.isScramble(s1[i:], s2[:-i]) and self.isScramble(s1[:i], s2[-i:]):
    #             return True
    #         if self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i], s2[:i]):
    #             return True
    #     return False

    def isScramble(self, s1, s2):
        if s1 == s2: return True
        if len(s1)!=len(s2): return False
        length = len(s1)
        # 3D DP
        # dp[i][j][k] = True means s1[i:i+(k+1)] and s2[j:j+(k+1)] are scramble strings
        dp = [[[False for i in range(length)] for j in range(length)] for k in range(length)]
        for i in range(length):
            for j in range(length):
                if s1[i] == s2[j]: dp[i][j][0] = True
        # bottom up
        for k in range(1, length):
            for i in range(length-k):
                for j in range(length-k):
                    for p in range(k):
                        if (dp[i][j][p] and dp[i+p+1][j+p+1][k-p-1]) or (dp[i][j+k-p][p] and dp[i+p+1][j][k-p-1]):
                            dp[i][j][k] = True; break
        return dp[0][0][length-1]

if __name__ == "__main__":
    s = Solution()
    print s.isScramble("great", "rgtae")
    print s.isScramble("great", "rgeat")
    print s.isScramble("great", "great")