class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        low = 0; high = x/2+1
        while low<=high:
            mid = (low+high)/2
            if mid**2 == x:
                return mid
            elif mid**2<x:
                low = mid+1
            else:
                high = mid-1
        return high

if __name__ == "__main__":
    s = Solution()
    print s.sqrt(10)
