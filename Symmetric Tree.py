class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None: return True
        return self.isSymmetricRecur(root.left, root.right)

    def isSymmetricRecur(self, node1, node2):
        if node1 is None or node2 is None: 
            if node1 is None and node2 is None: return True
            else: return False
        if node1.val!= node2.val: return False
        return self.isSymmetricRecur(node1.right, node2.left) and self.isSymmetricRecur(node1.left, node2.right)

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    print s.isSymmetric(root)
