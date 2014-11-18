class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one = 0; two = 0; 
        for num in A:
            three = ~(one|two)
            two = (two&~num)|(one&num)
            one = (one&~num)|(three&num)
        return one

if __name__ == "__main__":
    s = Solution()
    print s.singleNumber([2,2,2,5,8,8,8])
