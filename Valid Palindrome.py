class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s is None: return True
        left = 0; right = len(s)-1
        while left < right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            else:
                left+=1; right-=1
        return True

if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome("A man, a plan, a canal: Panama")
    print s.isPalindrome("race a car")
