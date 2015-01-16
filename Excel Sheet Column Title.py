class Solution:
    # @return a string
    def convertToTitle(self, num):
        res = ""
        while num>0:
            r = num%26; num=num/26
            if r==0: res = 'Z'+res; num-=1
            else: res = chr(ord('A')+r-1)+res
        return res

if __name__ == "__main__":
    s = Solution()
    print s.convertToTitle(52)
