import re

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        pattern = '^\s*(\+|\-)?([0-9]+(\.[0-9]+)?|\.[0-9]+|[0-9]+\.)(e(\+|\-)?[0-9]+)?\s*$'
        match = re.match(pattern, s)
        return match is not None

if __name__ == "__main__":
    s = Solution()
    print s.isNumber("   0.1e3   ")
    print s.isNumber("e")
    print s.isNumber(".1")
    print s.isNumber(".")
    print s.isNumber('3')