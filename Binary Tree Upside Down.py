class Solution:
    def upsidedown(self, root):
        if root is None: return None
        if root.left is None: return root
        new_root = self.upsidedown(root.left)
        new_left = self.upsidedown(root.right)
        root.left.left = new_left
        root.left.right = root
        root.left, root.right = None, None
        return new_root

if __name__ == "__main__":
    class TreeNode:
        def __init__(self, v):
            self.val = v
            self.left = None
            self.right = None
    s = Solution()
    root = TreeNode(1);root.left = TreeNode(2); root.right = TreeNode(3)
    root.left.left = TreeNode(4); root.left.right = TreeNode(5)
    root.right.left = TreeNode(6); root.right.right = TreeNode(7)
    res = s.upsidedown(root)
    print res.val, res.left.val, res.right.val, res.right.left.val, res.right.right.val
