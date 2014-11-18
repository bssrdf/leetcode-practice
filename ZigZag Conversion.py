class Solution:
    # @return a string
    def convert(self, s, nRows):
        if s is None or s == "" or nRows<=0: return ""
        if len(s)<=nRows or nRows == 1: return s
        res = ""; step = 2*nRows-2
        for i in range(nRows):
            for j in range(i, len(s), step):
                res += s[j]              
                if i > 0 and i < nRows-1 and j+step-2*i < len(s): 
                    res+=s[j+step-2*i]
        return res

if __name__ == "__main__":
    s = Solution()
    print s.convert("PAYPALISHIRING", 3)
    print s.convert("ABCDEF", 3)

