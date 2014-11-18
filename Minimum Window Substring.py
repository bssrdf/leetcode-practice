class Solution:
    # @return a string
    def minWindow(self, S, T):
        if S is None or T is None or len(S)==0 or len(T)==0: return ""
        mp = {t:-1 for t in T}; shortest = ""; start = 0; end = 0
        for i in range(len(S)):
            if (S[i] not in mp) and shortest == "": continue
            if (S[i] not in mp) and shortest != "":
                shortest = shortest+S[i]
                


