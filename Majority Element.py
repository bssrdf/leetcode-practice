class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, nums):
        lookup = {}
        for num in nums:
            if num not in lookup: lookup[num] = 1
            else: lookup[num] = lookup[num]+1
        for key in lookup.keys():
            if lookup[key] > len(nums)/2: return key

if __name__ == "__main__":
    s = Solution()
    print s.majorityElement([1,2,3,4,5,2,2,2,2,2])