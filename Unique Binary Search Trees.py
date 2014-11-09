class Solution:
    # @return an integer
    def numTrees(self, n):
        return self.numTreesRecur(range(n))

    def numTreesRecur(self, nums):
        if len(nums) == 0 or len(nums) == 1: return 1
        total = 0
        for i in range(len(nums)):
            left = self.numTreesRecur(nums[:i])
            right = self.numTreesRecur(nums[i+1:])
            total+= left*right
        return total

if __name__ == "__main__":
    s = Solution()
    print s.numTrees(3)

