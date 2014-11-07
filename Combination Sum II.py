class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        res = self.combinationSumRecur(sorted(candidates), target)
        return res

    def combinationSumRecur(self, candidates, target):
        found = []
        for i in range(len(candidates)):
            if candidates[i] == target:
                if [candidates[i]] not in found: found.append([candidates[i]])
            elif target-candidates[i] > 0:
                results = self.combinationSumRecur(candidates[i+1:], target-candidates[i])
                for result in results:
                    t = sorted([candidates[i]]+result)
                    if t not in found: found.append(t)
        return found

if __name__ == "__main__":
    s = Solution()
    print s.combinationSum2([10,1,2,7,6,1,5], 8)
    print s.combinationSum2([1,1], 1)