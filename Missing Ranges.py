class Solution:
    def missing(self, num, start, end):
        res = []; prev = start-1
        for i in range(len(num)+1):
            if i == len(num): cur = end+1
            else: cur = num[i]
            if (cur-prev)>1: res.append(self.printRange(prev+1, cur-1))
            prev = cur
        return res

    def printRange(self, start, end):
        if start==end: return str(start)
        else: return str(start)+"->"+str(end)

if __name__ == "__main__":
    s = Solution()
    print s.missing([0,1,3,50,75], 0, 99)