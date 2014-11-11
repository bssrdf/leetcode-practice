class Solution:
    # @return an integer
    def atoi(self, str):
        if len(str) == 0: return 0
        i = 0
        while i< len(str) and str[i] == ' ':
            i+=1
        if i == len(str): return 0
        sign = 1; result = 0
        if str[i] == '+' or str[i] == '-':
            if str[i] == '-': sign = -1
            i+=1
        while i < len(str) and str[i]>='0' and str[i]<='9':
            result = result*10 + int(str[i])
            i+=1
        return min(max(sign*result, -2147483648), 2147483647)

if __name__ == '__main__':
    s = Solution()
    print s.atoi("      ")
    print s.atoi("  -1000abcd") 

