class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        res = []
        self.partitionRecur(res, [], s, 0)
        return res

    def partitionRecur(self, res, cur, s, i):
        if i == len(s):
            res.append(cur)
        else:
            for j in range(i, len(s)):
                if self.isValidPalindrome(s[i:j+1]):
                    self.partitionRecur(res, cur+[s[i:j+1]], s, j+1)

    def isValidPalindrome(self, s):
        for i in range(len(s)/2):
            if s[i] != s[-(i+1)]: return False
        return True

if __name__ == "__main__":
    s = Solution()
    print s.partition("aab")
