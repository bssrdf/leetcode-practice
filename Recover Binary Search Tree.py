class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        current = root; prev_node = None; stack = []
        first, second = None, None
        while current is not None or len(stack)>0:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                if prev_node and node.val < prev_node.val:
                        if first is None:
                            first, second = prev_node, node
                        else:
                            second = node
                prev_node = node
                current = node.right
        first.val, second.val = second.val, first.val
        return root

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(1)
    new = s.recoverTree(root)
    print new.left.val










        