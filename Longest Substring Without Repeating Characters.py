class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        mp = {}; longest = 0; res = 0
        if s is None or len(s)==0: return 0
        for i in range(len(s)):
            if s[i] not in mp:                
                longest += 1
            else:
                longest = min(i-mp[s[i]], longest+1)
            mp[s[i]] = i
            res = max(res, longest)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring("abcabcbb")
    print s.lengthOfLongestSubstring("bbbbb")
    print s.lengthOfLongestSubstring("wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco")



