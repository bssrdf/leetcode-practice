class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m=len(A); n=len(B)
        if (m+n)%2==1: return self.findKth(A, B, (m+n)/2+1)
        else: return (self.findKth(A, B, (m+n)/2)+self.findKth(A, B, (m+n)/2+1))/2.0

    def findKth(self, A, B, k):
        if A is None or len(A)==0: return B[k-1]
        if B is None or len(B)==0: return A[k-1]
        m = len(A); n=len(B)
        midA = A[m/2]; midB = B[n/2]
        if (m+n)/2 >=k:
            if A[midA] >=B[midB]:
                return self.findKth(A[:midA], B, k)
            else:
                return self.findKth(A, B[:midB], k)
        else:
            if A[midA] <=B[midB]:
                return self.findKth(A[midA:], B, k-midA)
            else:
                return self.findKth(A, B[midB:], k-midB)

if __name__ == "__main__":
    s = Solution()
    print s.findMedianSortedArrays([1,2,3], [0, 1])
