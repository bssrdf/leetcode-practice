class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxSum = -9223372036854775808
        self.maxPathSumRecur(root)
        return self.maxSum

    def maxPathSumRecur(self, root):
        if root is None: return 0
        left = max(0, self.maxPathSumRecur(root.left))
        right = max(0, self.maxPathSumRecur(root.right))
        self.maxSum = max(self.maxSum, left+root.val+right)
        return root.val+max(left, right)

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print s.maxPathSum(root)


