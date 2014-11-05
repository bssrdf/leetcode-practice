class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if A is None or len(A)==0: return None
        if len(A)==1: return A[0]
        res_max = A[0]
        local_max = A[0]
        for i in range(1, len(A)):
            if local_max<=0:
                local_max = 0
            local_max+=A[i]
            res_max = max(res_max, local_max)
        return res_max

if __name__=="__main__":
    s = Solution()
    print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print s.maxSubArray([-2,1])