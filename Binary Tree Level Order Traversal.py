class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        if root is None: return result
        currents = [root]
        while currents:
            next = []; visited = []
            for current in currents:
                visited.append(current.val)
                if current.left: next.append(current.left)
                if current.right: next.append(current.right)
            currents = next
            result.append(visited)
        return result

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
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print s.levelOrder(root)

