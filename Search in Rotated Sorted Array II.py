class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        if A is None or len(A)==0: return False
        left = 0; right = len(A)-1
        while left<=right:
            mid = (left+right)/2
            if A[mid] == target: return True
            if A[mid]>A[left]:
                if target>=A[left] and target<A[mid]:
                    right = mid-1
                else:
                    left = mid+1
            elif A[mid]<A[left]:
                if target>A[mid] and target<=A[right]:
                    left = mid+1
                else:
                    right=mid-1
            else: # A[mid] == A[left]
                left+=1
        return False


if __name__ == "__main__":
    s = Solution()
    print s.search([6,7,1,2,3,4,5,5,5,5,6,6,6], 4)  
