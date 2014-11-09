class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None: return 0
        current = [root]; depth = 1
        while current:
            next = []
            for cur in current:
                if cur.left is None and cur.right is None: return depth
                if cur.left: next.append(cur.left)
                if cur.right: next.append(cur.right)
            current = next
            depth+=1
        return depth

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = TreeNode(0)
    root.left = TreeNode(1)
    print s.minDepth(root)

