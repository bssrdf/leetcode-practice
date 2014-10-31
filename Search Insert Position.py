class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if A is None: return None
        if len(A) == 0: return 0
        left = 0; right = len(A)-1
        while left <= right:
            mid = (left+right)/2
            if A[mid] == target: return mid
            elif A[mid]<target: left = mid+1
            else: right = mid-1
        return left

if __name__ == "__main__":
    s = Solution()
    print s.searchInsert([1,2,5,6], 5)
