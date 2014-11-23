class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        num.sort()
        return self.permuteRecur(num)

    def permuteRecur(self, num):
        if len(num) == 0 or num is None: return [[]]
        res = []
        for i in range(len(num)):
            remains = self.permuteRecur(num[:i]+num[i+1:])
            for remain in remains:
                if remain+[num[i]] not in res:
                    res.append(remain+[num[i]])
        return res

if __name__ == "__main__":
    s = Solution()
    t = [1,1]
    print s.permute(t)
    t = [1,0]
    print s.permute(t)