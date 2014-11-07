class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        res = self.combinationSumRecur(sorted(candidates), target)
        return res

    def combinationSumRecur(self, candidates, target):
        found = []
        for i in range(len(candidates)):
            if candidates[i] == target:
                found.append([candidates[i]])
            elif target-candidates[i] > 0:
                results = self.combinationSumRecur(candidates[i:], target-candidates[i])
                for result in results:
                    t = sorted([candidates[i]]+result)
                    found.append(t)
        return found

if __name__ == "__main__":
    s = Solution()
    print s.combinationSum([2,3,6,7], 7)

