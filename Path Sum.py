class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        return self.hasPathSumRecur(root, sum)

    def hasPathSumRecur(self, root, target):
        if root is None: return False
        if root.left is None and root.right is None:
            if root.val == target:
                return True
            else:
                return False
        return self.hasPathSumRecur(root.left, target-root.val) or self.hasPathSumRecur(root.right, target-root.val)
        
if __name__ == "__main__":
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = TreeNode(1)
    root.left = TreeNode(3)
    s = Solution()
    print s.hasPathSum(root, 4)