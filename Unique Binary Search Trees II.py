class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.generateTreesRecur(range(1, n+1))

    def generateTreesRecur(self, nums):
        res = []
        if len(nums) == 0: return [None]
        if len(nums) == 1: return [TreeNode(nums[0])]
        for i in range(len(nums)):
            left = self.generateTreesRecur(nums[:i])
            right = self.generateTreesRecur(nums[i+1:])
            for l in left:
                for r in right:
                    root = TreeNode(nums[i])
                    root.left = l; root.right = r
                    res.append(root)
        return res

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    res = s.generateTrees(3)
    print len(res)
