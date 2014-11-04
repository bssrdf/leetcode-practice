class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    # def rotate(self, matrix):
    #     return [list(reversed(i)) for i in zip(*matrix)]

    def rotate(self, matrix):
        for i in range(len(matrix)/2):
            first = i; last = len(matrix)-1-i
            for j in range(first, last):
                offset = j - first
                temp = matrix[first][j]
                # left to top
                matrix[first][j] = matrix[last-offset][first] 
                # bottom to left
                matrix[last-offset][first] = matrix[last][last-offset]
                # right to bottom
                matrix[last][last-offset] = matrix[j][last]
                # top to right
                matrix[j][last] = temp
        return matrix

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print s.rotate(matrix)