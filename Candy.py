class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        dp = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]: dp[i]=dp[i-1]+1
        for i in reversed(range(len(ratings)-1)):
            if ratings[i]>ratings[i+1] and dp[i]<=dp[i+1]: dp[i]=dp[i+1]+1
        return sum(dp)

if __name__ == "__main__":
    s = Solution()
    print s.candy([1,2,3,4,5])
    print s.candy([4,2,3,4,1])