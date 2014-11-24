class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    # check one by one
    # if encounter an '*', record its position
    # whenever cannot match, go back to recorded 'star' if exists, let '*' match one more char than previously
    def isMatch(self, s, p):
        pi, si, pp, ss = 0, 0, -1, -1
        while si<len(s):
            if pi<len(p) and (p[pi]=='?' or p[pi]==s[si]): pi+=1;si+=1; continue
            if pi<len(p) and p[pi]=='*': pp = pi; ss=si; pi+=1; continue
            if pp!=-1: pi=pp+1; ss+=1; si=ss; continue
            return False
        while pi<len(p) and p[pi]=='*':pi+=1
        return pi==len(p)

if __name__ == "__main__":
    s = Solution()
    print s.isMatch("aa","a"), False
    print s.isMatch("aa","aa"), True
    print s.isMatch("aaa","aa"), False
    print s.isMatch("aa", "*"), True
    print s.isMatch("aa", "a*"), True
    print s.isMatch("ab", "?*"), True
    print s.isMatch("aab", "c*a*b"), False