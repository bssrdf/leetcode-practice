class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A) == 0 or A is None: return -1
        left = 0; right = len(A)-1
        while left<=right:
            mid = (left+right)/2
            if A[mid]==target: return mid
            if A[mid] >= A[left]:
                if target<A[mid] and target>=A[left]:
                    right = mid-1
                else:
                    left = mid+1
            else: # A[mid] < A[left]
                if target>A[mid] and target<=A[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.search([6,7,1,2,3,4,5], 4)