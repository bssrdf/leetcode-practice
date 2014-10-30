class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == [] or matrix is None: return []
        res = []
        top=0;bottom=len(matrix)-1;left=0;right=len(matrix[0])-1
        while top<bottom and left<right:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            for i in range(top+1, bottom):
                res.append(matrix[i][right])
            for i in reversed(range(left, right+1)):
                res.append(matrix[bottom][i])
            for i in reversed(range(top+1, bottom)):
                res.append(matrix[i][left])
            top+=1;bottom-=1;left+=1;right-=1
        if top == bottom and left == right:
                res.append(matrix[top][left])
        elif top == bottom: 
            for i in range(left, right+1):
                res.append(matrix[top][i])
        elif left == right:
            for i in range(top, bottom+1):
                res.append(matrix[i][left])
        return res

if __name__ == "__main__":
    s = Solution()
    input = [[1,2,3],[4,5,6],[7,8,9]]
    output = s.spiralOrder(input)
    print output
