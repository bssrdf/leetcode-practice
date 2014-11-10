class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result = []; stack = []; current = root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                result.append(node.val)
                if node.right: current = node.right
        return result

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    node1 = TreeNode(1)
    node1.left = TreeNode(2)
    node1.right = TreeNode(3)
    res = s.inorderTraversal(node1)
    print res