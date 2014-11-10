class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.isBalancesRecur(root)[0]

    def isBalancesRecur(self, root):
        if root is None: return (True, 0)
        left = self.isBalancesRecur(root.left)
        right = self.isBalancesRecur(root.right)
        return (abs(left[1]-right[1])<=1 and left[0] and right[0], max(left[1], right[1])+1)

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print s.isBalanced(root)    