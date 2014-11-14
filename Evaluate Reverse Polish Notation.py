class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        st = []; 
        for i in tokens:
            if i!='+' and i!='*' and i!='/' and i!='-':
                st.append(int(i))
            else:
                b = st.pop()
                a = st.pop()
                if i=='+':
                    st.append(a+b)
                if i=='-':
                    st.append(a-b)
                if i=='*':
                    st.append(a*b)
                if i=='/':
                    st.append(int(a*1.0/b))
        return st.pop()

if __name__ == "__main__":
    s = Solution()
    print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])