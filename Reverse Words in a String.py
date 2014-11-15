class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return " ".join(filter(lambda x: x!="", reversed(s.split(" "))))

if __name__ == "__main__":
    s = Solution()
    print s.reverseWords("the sky  is blue ")

