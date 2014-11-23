class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        return self.permuteRecur(num)

    def permuteRecur(self, num):
        if len(num) == 0 or num is None: return [[]]
        res = []; prev = None
        for i in range(len(num)):
            if num[i] == prev: continue
            else: 
                prev = num[i]
                remains = self.permuteRecur(num[:i]+num[i+1:])
                for remain in remains:
                        res.append(remain+[num[i]])
        return res

if __name__ == "__main__":
    s = Solution()
    t = [1,1]
    print s.permuteUnique(t)
    t = [1,0]
    print s.permuteUnique(t)