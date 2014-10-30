class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        left=0; right=len(A)-1; middle=0;
        while middle < right:
            if A[middle]==0:
                A[left], A[middle] = 0, A[left]
                left+=1; 
            if A[middle]==2:
                A[right], A[middle]=2, A[right]
                right-=1; 
            if A[middle]==1:
                middle+=1

if __name__ == "__main__":
    s = Solution()
    input = [0,1,2,0,2,1]
    s.sortColors(input)
    print input   