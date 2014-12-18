class Solution:
    # @return boolean
    def oneEdit(self, S, T):
        if abs(len(S)-len(T))>1: return False
        if len(S)>len(T): return self.oneEdit(T, S)
        lenS = len(S); lenT = len(T)
        i = 0; shift = len(T)-len(S) # shift o or 1
        while i<lenS and S[i] == T[i]: i+=1
        if i==lenS: return shift == 1
        if shift==0: i+=1
        while i<lenS and S[i] == T[i+shift]: i+=1
        return i==lenS

if __name__ == "__main__":
    s = Solution()
    print s.oneEdit("aaa", "aba")
    print s.oneEdit("aaa", "abaa")
    print s.oneEdit("aaa", "aaab")
