class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        vers1 = [int(i) for i in version1.split(".")]
        vers2 = [int(i) for i in version2.split(".")]
        return self.compareVersionRecur(vers1, vers2)

    def compareVersionRecur(self, vers1, vers2):
        if len(vers1) == 0 and len(vers2)==0: return 0
        elif len(vers1) == 0: 
            if vers2[0] == 0: return self.compareVersionRecur(vers1, vers2[1:])
            else: return -1
        elif len(vers2) == 0: 
            if vers1[0] == 0: return self.compareVersionRecur(vers1[1:], vers2)
            else: return 1
        
        if vers1[0] == vers2[0]:
            return self.compareVersionRecur(vers1[1:], vers2[1:])
        elif vers1[0] > vers2[0]:
            return 1
        elif vers1[0] < vers2[0]:
            return -1

if __name__ == "__main__":
    s = Solution()
    print s.compareVersion("0.1","1.1")
    print s.compareVersion("1.2","1.1")
    print s.compareVersion("0.1","13.37")
    print s.compareVersion("13","13.37")
    print s.compareVersion("0013","13.37")
    print s.compareVersion("1.0", "1")