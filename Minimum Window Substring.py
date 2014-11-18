class Solution:
    # @return a string
    def minWindow(self, S, T):
        dictS, dictT = {}, {}
        for c in T: dictT[c] = dictT.get(c, 0)+1
        for c in dictT: dictS[c] = 0
        start, end = 0, 0
        total_cnt = 0; res = ""
        while end<len(S):
            # if char is found in T
            if S[end] in dictT:
                if dictS[S[end]] < dictT[S[end]]: total_cnt+=1
                dictS[S[end]] += 1
            # if all chars have been found for needed quantities
            if total_cnt == len(T):
                while start < len(S):
                    if S[start] in dictT:
                        if dictT[S[start]] == dictS[S[start]]: break # check out result
                        dictS[S[start]]-=1
                    start+=1
                # check out result
                if res == "" or len(res) > (end+1-start):
                    res = S[start:end+1]
            # in progress and char not needed
            end+=1
        return res

if __name__ == "__main__":
    s = Solution()
    S = "ADOBECODEBANC"
    T = "AB"
    print s.minWindow(S, T)




