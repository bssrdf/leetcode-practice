class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m=len(A); n=len(B)
        if (m+n)%2==1: return self.findKth(A, B, (m+n)/2+1)*1.0
        else: return (self.findKth(A, B, (m+n)/2)+self.findKth(A, B, (m+n)/2+1))/2.0

    # K starts from 1
    def findKth(self, A, B, k):
        if len(A)==0: return B[k-1]
        if len(B)==0: return A[k-1]
        m = len(A); n=len(B)
        if (m/2+n/2+1) < k:
            if A[m/2] > B[n/2]:
                print A, B, k, "->", A, B[n/2+1:], k-n/2-1, "case1"
                return self.findKth(A, B[n/2+1:], k-n/2-1)
            else:
                print A, B, k, "->", A[m/2+1:], B, k-m/2-1, "case2"
                return self.findKth(A[m/2+1:], B, k-m/2-1)
        else:
            if A[m/2] > B[n/2]:
                print A, B, k, "->", A[:m/2], B, k, "case3"
                return self.findKth(A[:m/2], B, k)
            else:
                print A, B, k, "->", A, B[:n/2], k, "case4"
                return self.findKth(A, B[:n/2], k)

if __name__ == "__main__":
    s = Solution()
    print s.findMedianSortedArrays([1,2,3], [0,1])
    print s.findMedianSortedArrays([1,2,3], [1])
    print s.findMedianSortedArrays([1,2], [1,2,3])
    print s.findMedianSortedArrays([1,2,3], [1,2])
    print s.findMedianSortedArrays([1,2], [1,2])
    print s.findMedianSortedArrays([1,2,3], [1,2,3])
    print s.findMedianSortedArrays([1,2,5,10], [2,5,7])
    print s.findMedianSortedArrays([1,2,3,4,5], [6,7,8,9,10])
    print s.findMedianSortedArrays([1],[1])