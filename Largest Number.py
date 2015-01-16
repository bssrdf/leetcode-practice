class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted([str(x) for x in num], cmp=self.compare)
        ans = ''.join(num).lstrip('0')
        return ans or '0'

    def compare(self, a, b):
        return -1 if a+b>b+a else 1

if __name__ == "__main__":
    s = Solution()
    print s.largestNumber([3, 30, 34, 5, 9])