class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        cur = [[]]
        for s in sorted(S):
            next = []
            for candidate in cur:
                if (candidate+[]) not in next: next.append(candidate+[])
                if (candidate+[s]) not in next: next.append(candidate+[s])
            cur=next
        return cur

if __name__ == "__main__":
    s = Solution()
    print s.subsetsWithDup([1, 2, 2])
    