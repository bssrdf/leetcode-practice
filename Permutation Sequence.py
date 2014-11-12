import math

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        res, k, fact = "", k-1, math.factorial(n-1)
        num = [i for i in range(1, n+1)]
        for i in reversed(range(n)):
            curr = num[k/fact]
            res += str(curr)
            num.remove(curr)
            if i>0:
                k%=fact
                fact/=i
        return res

if __name__ == "__main__":
    s = Solution()
    print s.getPermutation(3, 2)  
            

