class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 1: return triangle[0][0]
        next = [0 for i in range(len(triangle))]
        next[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            next[i] = triangle[i][i]+next[i-1]
            for j in reversed(range(1, i)):
                next[j] = min(next[j], next[j-1])+triangle[i][j]
            next[0] = triangle[i][0]+next[0]
        return min(next)

if __name__ == "__main__":
    s = Solution()
    tri = [
                 [2],
                [3,4],
               [6,5,7],
              [4,1,8,3]
            ]
    print s.minimumTotal(tri)                

