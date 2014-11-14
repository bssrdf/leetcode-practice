class Solution:
    # @return a boolean
    def isValid(self, s):
        dict = {"(":")", "[":"]", "{":"}"}
        st = []
        for i in s:
            if i in dict: st.append(i)
            else:
                if len(st) == 0: return False
                if dict[st[-1]] != i: return False
                st.pop()
        if len(st) == 0: return True
        return False

if __name__ == "__main__":
    s=Solution()
    print s.isValid("()[]{}")
    print s.isValid("([)])")


