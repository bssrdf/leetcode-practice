class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ""
        strs.sort(key=lambda x: len(x))
        longest = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(longest):
                if longest[i]!=s[i]: 
                    longest = s[:i]
                    break
                i += 1
        return longest

if __name__ == "__main__":
    s = Solution()
    print s.longestCommonPrefix(["shen", "sh"])
