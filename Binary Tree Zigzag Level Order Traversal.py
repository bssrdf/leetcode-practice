class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        current, res, lefttoright = [root], [], True
        while current:
            next, vals = [], []
            while current:
                node = current.pop()
                vals.append(node.val)
                if not lefttoright:
                    if node.right: next.append(node.right)
                    if node.left: next.append(node.left)
                else:
                    if node.left: next.append(node.left)
                    if node.right: next.append(node.right)
            lefttoright = not lefttoright        
            res.append(vals[:])
            current = next
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
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    res = s.zigzagLevelOrder(root)
    print res
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    res = s.zigzagLevelOrder(root)
    print res
