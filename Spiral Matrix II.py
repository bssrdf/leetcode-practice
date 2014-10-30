class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        A = [i for i in range(1, n*n+1)]
        res = [[1 for i in range(n)] for i in range(n)]
        top = 0; bottom = n-1; left = 0; right = n-1
        while top < bottom and left < right:
            for i in range(left, right+1):
                res[top][i] = A.pop(0)
            for i in range(top+1, bottom):
                res[i][right] = A.pop(0)
            for i in reversed(range(left, right+1)):
                res[bottom][i] = A.pop(0)
            for i in reversed(range(top+1, bottom)):
                res[i][left] = A.pop(0)
            top+=1;bottom-=1;left+=1;right-=1
        if n%2==1: res[top][left]=n*n
        return res

if __name__ == "__main__":
    s = Solution()
    print s.generateMatrix(3)