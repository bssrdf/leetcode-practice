class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        fast_check = {word:False for word in dict}; fast_check[end]=False 
        currents = [start]; length = len(start); distance = 0
        while len(currents)!=0:
            next = []; distance += 1
            for word in currents:
                for i in range(length):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                            candidate = word[:i]+c+word[i+1:]
                            if candidate == end: return distance+1
                            else: 
                                if candidate in fast_check and fast_check[candidate]==False:
                                    fast_check[candidate] = True
                                    next.append(candidate)
            currents = next
        return 0

if __name__ == "__main__":
    s = Solution()
    start, end = "hit", "cog"
    dict = set(["hot", "dot", "dog", "lot", "log"])
    print s.ladderLength(start, end, dict)
    start, end = "game", "thee"
    dict = set(["frye","heat","tree","thee","game","free","hell","fame","faye"])
    print s.ladderLength(start, end, dict)






