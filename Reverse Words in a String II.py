class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = list(s)
        self.reverse(s, 0, len(s)-1)
        start = 0; curr = 0
        while curr<len(s):
            if s[curr]!=' ': curr+=1
            else:
                end = curr-1
                self.reverse(s, start, end)
                curr+=1
                start=curr
        return "".join(s)

    def reverse(self, s, i, j):
        while i<j:
            s[i], s[j] = s[j], s[i]

if __name__ == "__main__":
    s = Solution()
    print s.reverseWords("the sky is blue")

