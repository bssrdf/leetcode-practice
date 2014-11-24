class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j] and ((j-i)<=2 or dp[i+1][j-1]):
                    dp[i][j] = True
        min_cut = [0 for i in range(len(s))]
        for i in range(len(s)):
            cur_min = 9223372036854775807
            if dp[0][i]: cur_min = 0
            else:
                for j in range(1, i+1):
                    if dp[j][i]: cur_min = min(cur_min, min_cut[j-1]+1)
            min_cut[i] = cur_min
        return min_cut[-1]

if __name__ == "__main__":
    s = Solution()
    print s.minCut("aab")
    print s.minCut("efe")