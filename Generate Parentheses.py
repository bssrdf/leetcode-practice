class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n <= 0: return [""]
        res = []
        self.generateParenthesisRecur(res, "(", n-1, n)
        return res

    def generateParenthesisRecur(self, res, cur, left, right):
        if left>right: return
        else:
            if left == 0 and right == 1:
                res.append(cur+")"); return
            elif left == 0:
                self.generateParenthesisRecur(res, cur+")", left, right-1)
            elif left > 0:
                self.generateParenthesisRecur(res, cur+"(", left-1, right)
                self.generateParenthesisRecur(res, cur+")", left, right-1)
            else:
                return

if __name__ == "__main__":
    s = Solution()
    print s.generateParenthesis(3)




