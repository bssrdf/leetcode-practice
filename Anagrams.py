class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dictionary = {}
        for string in strs:
            if str(sorted(string)) not in dictionary:
                dictionary[str(sorted(string))] = [string]
            else:
                dictionary[str(sorted(string))].append(string)
        res = []
        for elem in dictionary:
            if len(dictionary[elem])>1:
                res = res + dictionary[elem]
        return res

if __name__ == "__main__":
    s = Solution()
    t = ["eat", "ate", "eta", "yes"]
    print s.anagrams(t)
