class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root is None: return 0
        if root.left is None and root.right is None: return root.val
        return self.sumNumbersRecur(root.left, root.val)+self.sumNumbersRecur(root.right, root.val)

    def sumNumbersRecur(self, node, prevsum):
        if node is None: return 0
        if node.left is None and node.right is None:
            return prevsum*10+node.val
        return self.sumNumbersRecur(node.left, prevsum*10+node.val)+self.sumNumbersRecur(node.right, prevsum*10+node.val)

if __name__=="__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print s.sumNumbers(root)
