class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0: return False
        num_of_digits = 0
        current = x
        while current > 0:
            num_of_digits+=1
            current/=10
        if num_of_digits == 1: return True
        p = x; q = 0; i = 0
        while i < num_of_digits/2:
            q = q*10 + p%10
            p /= 10
            i+=1
        if num_of_digits%2 == 1:
            p /= 10
        if p == q: return True
        return False

if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome(2147483647)
    print s.isPalindrome(1234567890987654321)