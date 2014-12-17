class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        low = 0; high = len(num)-1
        while low<high:
            mid = (low+high+1)/2
            if mid==0 or num[mid]>num[mid-1]:
                low = mid
            else:
                high = mid-1
        return low

if __name__ == "__main__":
    s = Solution()
    print s.findPeakElement([1,2,3,1])