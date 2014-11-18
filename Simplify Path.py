class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        paths = filter(lambda x: x!="", path.split("/"))
        st = []
        for p in paths:
            if p == '.': pass
            elif p == '..': 
                if len(st)>0: st.pop()
            else:
                st.append(p)
        res = "/"+"/".join(st)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.simplifyPath("/home/me")
    print s.simplifyPath("/a/./b/../../c/")

