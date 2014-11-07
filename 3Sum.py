class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, nums):
        if nums is None or len(nums) == 0: return []
        nums.sort()
        res = []; i = 0
        while i < len(nums)-2:
            j = i+1; k = len(nums)-1
            while j < k :
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1; k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
            i+=1
            while i<len(nums)-2 and nums[i]==nums[i-1]:
                i+=1
        return res

if __name__ == '__main__':
    s = Solution()
    A = [-1,0,1,2,-1,-4]
    print s.threeSum(A)
    B = [0,0,0,0,0,0,0]
    print s.threeSum(B)




