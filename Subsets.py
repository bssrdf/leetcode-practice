class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        currents = [[]]
        for s in S:
            next = []
            for current in currents:
                next.append(current)
                next.append(current+[s])
            currents = next
        return currents

if __name__ == "__main__":
    s = Solution()
    print s.subsets([4,1,0])