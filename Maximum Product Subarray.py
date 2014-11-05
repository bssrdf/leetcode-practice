class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if A is None or len(A)==0: return None
        if len(A)==1: return A[0]
        res_max = A[0]
        local_max = [0 for i in range(len(A))]; local_min = [0 for i in range(len(A))]
        local_min[0] = A[0]; local_max[0] = A[0]
        for i in range(1, len(A)):
            var_max = max(A[i], local_min[i-1]*A[i], local_max[i-1]*A[i])
            local_max[i] = var_max
            var_min = min(A[i], local_min[i-1]*A[i], local_max[i-1]*A[i])
            local_min[i] = var_min
            res_max = max(res_max, local_max[i])
        return res_max

if __name__ == "__main__":
    s = Solution()
    print s.maxProduct([2,3,-2,4])
    print s.maxProduct([-1,-2,-9,-6])