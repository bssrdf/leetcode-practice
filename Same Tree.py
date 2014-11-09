class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None or q is None:
            if p is None and q is None: return True
            else: return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    p = TreeNode(0)
    p.left = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(0)
    q.left = TreeNode(1)
    q.left = TreeNode(2)
    print s.isSameTree(p, q)