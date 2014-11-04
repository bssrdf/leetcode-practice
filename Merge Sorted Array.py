class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if m==0: 
            for i in range(n):
                A[i] = B[i]
            return
        if n==0: return
        end = m + n -1
        indexA, indexB = m-1, n-1
        while indexA>=0 and indexB>=0:
            if A[indexA]>B[indexB]: 
                A[end] = A[indexA]
                end-=1; indexA-=1
            else:
                A[end]=B[indexB]
                end-=1; indexB-=1
        if indexB>=0:
            for i in range(indexB+1):
                A[i]=B[i]

if __name__ == "__main__":
    s = Solution()
    A = [1,2,3,6,7,8,None, None, None]
    B = [4,5,6]
    s.merge(A,6,B,3)
    print A, B
