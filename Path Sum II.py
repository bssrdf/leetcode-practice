class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None: return []
        res = []
        self.pathSumRecur(root, sum, res, [])
        return res

    def pathSumRecur(self, root, target, res, cur):
        if root is None: return
        if root.left is None and root.right is None:
            if root.val == target:
                res.append(cur+[root.val])
            return
        self.pathSumRecur(root.left, target-root.val, res, cur+[root.val])
        self.pathSumRecur(root.right, target-root.val, res, cur+[root.val])

if __name__ == "__main__":
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    s = Solution()
    print s.pathSum(root, 22)