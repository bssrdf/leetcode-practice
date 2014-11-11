class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n<0: return 1.0/self.pow(x, -n)
        if n==0: return 1.0
        if n%2==0: return self.pow(x*x, n/2)
        if n%2==1: return x*self.pow(x*x, (n-1)/2)

if __name__ == "__main__":
    s = Solution()
    print s.pow(2.0, 3)
    print s.pow(-1.0, 3)
    print s.pow(-2, -3) 

