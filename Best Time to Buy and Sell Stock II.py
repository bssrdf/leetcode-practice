class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices)==1: return 0
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(0, prices[i]-prices[i-1])
        return max_profit

if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([1,2,3,4,5])