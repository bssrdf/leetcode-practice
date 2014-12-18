# class Solution:
#     # @param s, a string
#     # @param dict, a set of string
#     # @return a list of strings
#     def wordBreak(self, s, dict):
#         mp = {}
#         dp = [False for i in range(len(s))]
#         for i in reversed(range(len(s))):
#             mp[s[i:]] = []
#             for j in range(i, len(s)):
#                 if s[i:j+1] in dict:
#                     if j == len(s)-1:
#                         dp[i] = True; mp[s[i:]].append(s[i:])
#                     elif dp[j+1]:
#                         dp[i] = True; 
#                         for candidate in mp[s[j+1:]]:
#                             mp[s[i:]].append(s[i:j+1]+" "+candidate)
#         return mp[s]

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        mp = {s[:i+1]:[] for i in range(len(s))}
        dp = [False for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] in dict and (j==0 or dp[j-1]):
                    dp[i] = True
                    if j==0: mp[s[:i+1]].append(s[:i+1])
                    else: mp[s[:i+1]].extend([e+" "+s[j:i+1] for e in mp[s[:j]]])
        return mp[s]

if __name__ == "__main__":
    s = Solution()
    print s.wordBreak("catsanddog", ["cats", "cat", "and", "sand", "dog"])
    print s.wordBreak("a", [])