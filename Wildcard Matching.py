class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):


if __name__ == "__main__":
    s = Solution()
    print s.isMatch("aa","a"), False
    print s.isMatch("aa","aa"), True
    print s.isMatch("aaa","aa"), False
    print s.isMatch("aa", "*"), True
    print s.isMatch("aa", "a*"), True
    print s.isMatch("ab", "?*"), True
    print s.isMatch("aab", "c*a*b"), False