class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        dp = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                dp[i+j+1] += int(num1[i])*int(num2[j])
        carry = 0
        for i in reversed(range(len(dp))):
            dp[i], carry = (dp[i]+carry)%10, (dp[i]+carry)/10          
        for i in range(len(num1)+len(num2)-1):
            if dp[i] != 0: break
            i += 1
        res = ''
        for d in range(i, len(num1)+len(num2)):
            res = res + str(dp[d])
        return res

if __name__ == "__main__":
    s = Solution()
    print s.multiply('999', '999')
    print s.multiply('0', '0')
    print s.multiply('98', '9')


