class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None: return
        self.flattenRecur(root)

    def flattenRecur(self, root):
        if root.left is None and root.right is None:
            return (root, root)
        elif root.left is None:
            right = self.flattenRecur(root.right)
            return (root, right[1])
        elif root.right is None:
            left = self.flattenRecur(root.left)
            root.right = left[0]
            root.left = None
            return (root, left[1])
        else:
            left = self.flattenRecur(root.left)
            right = self.flattenRecur(root.right)
            root.left = None
            root.right = left[0]; left[1].right = right[0]
            return (root, right[1])

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    node1, node2, node3, node4, node5, node6 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4
    node5.right = node6
    s.flatten(node1)
    while node1 is not None:
        print node1.val,
        node1 = node1.right


