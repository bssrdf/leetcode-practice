class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0: return "NaN"
        if numerator == 0: return "0"
        res = ""
        if numerator*denominator<0: res+="-"
        n = abs(numerator); d = abs(denominator)
        res+=str(n/d)
        if n%d == 0: return res
        else: res+="."
        lookup = {}; r = n%d
        while r>0:
            if r in lookup:
                pos = lookup[r]
                res = res[:pos]+"("+res[pos:]+")"
                break
            lookup[r] = len(res)
            res+=str(r*10/d)
            r=(r*10)%d
        return res

if __name__ == "__main__":
    s = Solution()
    print s.fractionToDecimal(1,2)
    print s.fractionToDecimal(2,1)
    print s.fractionToDecimal(2,3)
    print s.fractionToDecimal(1,7)


