class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        first_row = 1; first_col = 1
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col = 0
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                first_row = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if first_row == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if first_col == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

if __name__ == "__main__":
    s = Solution()
    m = [
      [1, 1, 1, 0, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 0, 1, 1, 1],
      [1, 0, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 0, 1, 1, 1, 1]
    ]
    for i in m:
        print i
    print
    s.setZeroes(m)
    for i in m:
        print i
    print
