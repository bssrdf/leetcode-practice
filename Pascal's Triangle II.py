class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        prev = [1]
        for i in range(1, rowIndex+1):
            temp = 1
            for j in range(1, len(prev)):
                value = temp+prev[j]
                temp = prev[j]
                prev[j] = value
            prev.append(1)
        return prev

if __name__ == "__main__":
    s = Solution()
    print s.getRow(3)
