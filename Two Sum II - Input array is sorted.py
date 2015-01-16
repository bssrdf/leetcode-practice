class Solution:
    def twoSum(self, nums, target):
        i = 0; j = len(nums)-1
        while i<j and nums[i]+nums[j]!=target:
            if nums[i]+nums[j]<target: i+=1
            elif nums[i]+nums[j]>target: j-=1
        return (i+1, j+1)

if __name__ == "__main__":
    s = Solution()
    print s.twoSum([2,7,11,15], 9)

