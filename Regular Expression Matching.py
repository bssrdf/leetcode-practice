class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp = [[False for i in range(len(s)+1)] for j in range(len(p)+1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            if p[i-1] == '*' and i-2>=0: dp[i][0] = dp[i-2][0]
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or (dp[i][j-1] and (s[j-1]==p[i-2] or p[i-2]=='.')) # zero, one or more than one preceding char
                elif p[i-1] == '.' or p[i-1]==s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[len(p)][len(s)]

if __name__ == "__main__":
  s = Solution()
  print s.isMatch("aa","a"), False
  print s.isMatch("aa","aa"), True
  print s.isMatch("aaa","aa"), False
  print s.isMatch("aa", "a*"), True
  print s.isMatch("aa", ".*"), True
  print s.isMatch("ab", ".*"), True
  print s.isMatch("aab", "c*a*b"), True
  print s.isMatch("aaa", "a*a"), True
  print s.isMatch("bbbba", ".*a*a"), True
  print s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"), False