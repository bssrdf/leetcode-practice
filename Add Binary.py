class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        m = len(a)-1; n = len(b)-1
        res = ''; carry = 0
        while m>=0 or n>=0:
            value = 0
            if m>=0: value+=int(a[m]); m-=1
            if n>=0: value+=int(b[n]); n-=1
            value+=carry
            value, carry = value%2, value/2
            res = str(value)+res
        if carry == 1: res = '1'+res
        return res

if __name__ == "__main__":
    s = Solution()
    print s.addBinary("11", "1")

