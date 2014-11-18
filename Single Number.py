class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for num in A:
            res = res^num
        return res

if __name__ == "__main__":
    s = Solution()
    print s.singleNumber([2,2,4,4,6]) 