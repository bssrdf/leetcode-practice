class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if s is None or len(s)<=1: return 0
        dp = [0 for i in range(len(s))] # longest parentheses started at idx i
        longest = 0
        for i in reversed(range(len(s)-1)):
            if s[i] == ")": dp[i] = 0
            else:
                j = i+dp[i+1]+1
                if j<len(s) and s[j] == ')': 
                    dp[i] = dp[i+1]+2
                    if (j+1)<len(s): dp[i]+=dp[j+1]
            longest = max(longest, dp[i])
        return longest

if __name__ == "__main__":
    s = Solution()
    print s.longestValidParentheses(")()())")
                

        
        