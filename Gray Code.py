class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n <=0: return [0]
        if n == 1: return [0, 1]
        remains = self.grayCode(n-1)
        res = []
        for remain in remains:
            res.append(remain)
        for i in reversed(range(len(remains))):
            res.append((1<<(n-1))+remains[i])
        return res

if __name__ == "__main__":
    s = Solution()
    print s.grayCode(2)

