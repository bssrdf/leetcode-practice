class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s is None: return 0
        current = 0; length = 0
        for i in reversed(range(len(s))):
            if s[i] == ' ' and length == 0: pass
            if s[i] != ' ': length +=1
            if s[i] == ' ' and length > 0: break
        return length

if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLastWord("Hello World")
    print s.lengthOfLastWord(" World ")
    print s.lengthOfLastWord("World")

