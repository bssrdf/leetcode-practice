class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        lenW = len(L[0])
        lenL = len(L)
        lenS = len(S)
        res = []
        for start in range(lenS-lenW*lenL+1):
            listS = [S[i:i+lenW] for i in range(start, start+lenW*lenL, lenW)]
            found = True
            for word in L:
                if word in listS: listS.remove(word)
                else: found = False; break
            if found == True: res.append(start)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.findSubstring("barfoothefoobarman", ["foo","bar"]) 
