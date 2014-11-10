class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None:
            return []
        res, current = [], [root]
        while current:
            next, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            current = next
            res.insert(0, vals)
        return res

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    print s.levelOrderBottom(root)
        