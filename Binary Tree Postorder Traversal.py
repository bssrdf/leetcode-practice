class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        res = []; stack = []; current = root
        while current or stack:
            if current:
                res.append(current.val)
                stack.append(current)
                current = current.right
            else:
                node = stack.pop()
                if node.left: current = node.left
        return list(reversed(res))

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print s.postorderTraversal(root)

