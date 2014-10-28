class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        lookup = {}
        for i, e in enumerate(num):
            j = target - e
            if j in lookup:
                return (lookup[j]+1, i+1)
            lookup[e] = i

if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print s.twoSum(nums, target)   