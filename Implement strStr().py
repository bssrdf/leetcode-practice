class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        # KMP
        if needle is None or needle == '': return 0
        if haystack is None or haystack == '': return -1
        lps = [0 for i in range(len(needle))]; j = 0
        for i in range(1, len(needle)):
            while needle[i]!=needle[j] and j>0: j = lps[j-1]
            if needle[i]==needle[j]: j+=1
            lps[i] = j
        t, p = 0, 0
        while t<len(haystack):
            while p>0 and (p==len(needle) or needle[p]!=haystack[t]):
                if p == len(needle): return t-p
                p = lps[p-1]
            if needle[p] == haystack[t]:t+=1;p+=1
            if p==0 and needle[p]!=haystack[t]: t+=1
        if p == len(needle): return t-p
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.strStr("Yiran Shen", "ran")
    print s.strStr("Yiran Shen", "no") 
    print s.strStr("a", "a") 

