class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        mp = {"1": "", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if digits is None or digits == "": return [""]
        res = []
        remains = self.letterCombinations(digits[1:])
        for remain in remains:
            for candidate in mp[digits[0]]:
                res.append(candidate+remain)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations("234")