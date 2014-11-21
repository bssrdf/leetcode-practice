class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        return self.combineRecur(range(1, n+1), k)

    def combineRecur(self, nums, k):
        if k<=0 or k>=len(nums)+1: return [[]] 
        if len(nums)<=0: return [[]]
        res = []
        remains = self.combineRecur(nums[1:], k-1)
        for remain in remains:
            res.append([nums[0]]+remain)
        remains = self.combineRecur(nums[1:], k)
        for remain in remains:
            if remain: res.append(remain)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.combine(5, 3)
