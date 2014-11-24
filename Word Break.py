class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        dp = [False for i in range(len(s))]
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i:j+1] in dict:
                    if j+1<len(s) and dp[j+1]:
                        dp[i] = True; break
                    elif j == len(s)-1:
                        dp[i] = True; break
        return dp[0]

if __name__ == "__main__":
    s = Solution()
    print s.wordBreak("leetcode", ["leetcode", "code"])



