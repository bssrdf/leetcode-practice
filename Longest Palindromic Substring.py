class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if s is None: return ""
        longest = ""
        for i in range(len(s)):
            substring = self.expandAroundCenter(s, i, i)
            if len(substring) > len(longest): longest = substring
        for i in range(len(s)-1):
            substring = self.expandAroundCenter(s, i, i+1)
            if len(substring) > len(longest): longest = substring
        return longest 

    def expandAroundCenter(self, s, left, right):
        while left>=0 and right<=len(s)-1 and s[left]==s[right]:
            left-=1; right+=1
        return s[left+1:right]

if __name__ =="__main__":
    s = Solution()
    print s.longestPalindrome("abacdfgdcaba")
    print s.longestPalindrome("abb")

            


