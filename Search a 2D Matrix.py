class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        start = 0; end = len(matrix)*len(matrix[0])-1
        while start<=end:
            mid = (start+end)/2
            row = mid/len(matrix[0])
            col = mid%len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid-1
            else:
                start = mid+1
        return False

if __name__ == "__main__":
    s = Solution()
    a = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
    print s.searchMatrix(a, 3)