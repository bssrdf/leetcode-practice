class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        if s is None: return []
        res = []
        self.restoreIpAddressesRecur(res, "", s, 4)
        return res

    def restoreIpAddressesRecur(self, res, cur, s, cnt):
        if cnt == 0:
            if len(s) == 0:
                res.append(cur[:-1]); return
            else:
                return
        else:
            if len(s)<cnt or len(s)>3*cnt:
                return
            else:
                if len(s)>=1: self.restoreIpAddressesRecur(res, cur+s[:1]+".", s[1:], cnt-1)
                if len(s)>=2 and s[:2]>='10' and s[:2]<='99': self.restoreIpAddressesRecur(res, cur+s[:2]+".", s[2:], cnt-1)
                if len(s)>=3 and s[:3]>='100' and s[:3]<='255': self.restoreIpAddressesRecur(res, cur+s[:3]+".", s[3:], cnt-1)

if __name__ == "__main__":
    s = Solution()
    print s.restoreIpAddresses("25525511135")
    print s.restoreIpAddresses("010010")




