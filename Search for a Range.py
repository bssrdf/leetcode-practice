class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        res = []
        start, end = 0, len(A)-1
        while start<end:
            mid = (start+end)/2
            if target<=A[mid]:
                end = mid
            else:
                start = mid+1
        if A[start]!=target: return [-1,-1]
        res.append(start)
        start, end = 0, len(A)
        while start<end:
            mid=(start+end)/2
            if target>=A[mid]:
                start = mid+1
            else:
                end = mid
        res.append(start-1)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.searchRange([2,2], 2)
    print s.searchRange([5,7,7,8,8,10], 8)