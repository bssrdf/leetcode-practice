class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry = 1
        for i in reversed(range(len(digits))):
            value = (digits[i]+carry)%10
            carry = (digits[i]+carry)/10
            digits[i] = value
        if carry!=0: digits.insert(0, carry)
        return digits

if __name__ == "__main__":
    s = Solution()
    print s.plusOne([9, 9, 9])