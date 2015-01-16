class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack)!=0

    # @return an integer, the next smallest number
    def next(self):
        top = self.stack.pop()
        self.pushLeft(top.right)
        return top.val

    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        
if __name__ == "__main__":
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = TreeNode(4); root.left = TreeNode(2); root.right = TreeNode(6)
    root.left.right = TreeNode(3); root.right.left = TreeNode(5)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v