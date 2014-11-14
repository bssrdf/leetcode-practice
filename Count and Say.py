class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1: return "1"
        current = "1"
        for j in range(2, n+1):
            next = ""
            prev = ""; cnt = 0; i = 0
            while i<len(current):
                if current[i]!= prev:
                    if i!=0: next = next + str(cnt) + prev
                    prev = current[i]; cnt=1
                else:
                    cnt+=1
                i+=1
            next = next + str(cnt) + prev
            current = next
        return current

if __name__ == "__main__":
    s = Solution()
    print s.countAndSay(7)

            


