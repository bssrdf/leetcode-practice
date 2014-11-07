class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        min_price = 9223372036854775807; max_profit = 0; max_profits = []
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i]-min_price)
            max_profits.append(max_profit)
        max_price = 0; max_profit_after = 0; max_profit_combined = 0
        for i in reversed(range(len(prices))):
            max_price = max(max_price, prices[i])
            max_profit_after = max(max_profit_after, max_price-prices[i])
            max_profit_combined = max(max_profit_combined, max_profit_after+max_profits[i])
        return max_profit_combined

if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([1,2,3,4,5])
    print s.maxProfit([2,1,2,0,1])