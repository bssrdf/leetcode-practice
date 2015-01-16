class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        res = 0
        for i in range(len(s)):
            res += (ord(s[i])-64)*26**(len(s)-1-i)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.titleToNumber('AZ')
