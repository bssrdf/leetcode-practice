class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = 1
        if dividend < 0: sign = -sign
        if divisor < 0: sign = -sign
        m = abs(dividend); n = abs(divisor)
        res = 0; c = 1
        while m > n: n <<= 1; c <<= 1
        while m >= abs(divisor):
            while m >= n: m-=n; res+=c
            n >>= 1; c>>=1
        return -res if sign==-1 else res

if __name__ == "__main__":
    s = Solution()
    print s.divide(10, -3)
    print s.divide(1, 1)




        