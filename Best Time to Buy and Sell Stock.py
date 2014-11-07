class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices)==1: return 0
        max_profit = 0; local_min = prices[0]
        min_prices = [0 for i in range(len(prices))]
        for i in range(len(prices)):
            min_prices[i] = local_min
            local_min = min(local_min, prices[i])
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i]-min_prices[i])
        return max_profit

if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([1,2,3,4,5])

