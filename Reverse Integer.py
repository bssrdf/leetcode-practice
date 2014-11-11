class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0: return 0
        sign = 1
        if x<0: sign = -1
        res = 0; x=abs(x)
        while x!=0:
            last_digit = x%10
            res = res*10 + last_digit
            x = x/10
        return sign*res

if __name__ == "__main__":
    s = Solution()
    print s.reverse(-123)

