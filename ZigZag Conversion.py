class Solution:
    # @return a string
    def convert(self, s, nRows):
        if s is None or s == "" or nRows<=0: return ""
        if len(s)<=nRows or nRows == 1: return s
        res = ""
        for i in range(nRows):
            while i < len(s):
                res += s[i]
                if i > 0 and i < nRows-1: 
                    if i+2*nRows-2-2*i < len(s): 
                        res+=s[i+2*nRows-2-2*i]
                i+=2*nRows-2
        return res

if __name__ == "__main__":
    s = Solution()
    print s.convert("PAYPALISHIRING", 3)
    print s.convert("ABCDEF", 3)

