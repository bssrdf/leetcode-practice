import math

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        res = 0; m = 5
        while n>=m:
            res += n/m; m*=5
        return res

if __name__ == "__main__":
    s = Solution()
    print math.factorial(25), s.trailingZeroes(25)
