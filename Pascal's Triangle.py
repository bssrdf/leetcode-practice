class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        res = [[1]]
        prev = [1]
        for i in range(2, numRows+1):
            temp = []
            temp.append(1)
            for j in range(i-2):
                temp.append(prev[j]+prev[j+1])
            temp.append(1)
            prev = temp
            res.append(temp)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.generate(5)
