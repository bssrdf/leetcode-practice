class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []; stack = []; current = root 
        while current or stack:
            if current:
                result.append(current.val)
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                if node.right: current = node.right
        return result

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
    print s.preorderTraversal(root)


