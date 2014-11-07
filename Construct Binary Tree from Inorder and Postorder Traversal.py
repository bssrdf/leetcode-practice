class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        root = self.buildTreeRecur(inorder, postorder)
        return root

    def buildTreeRecur(self, inorder, postorder):
        if len(inorder) == 0: return None
        if len(inorder) == 1: return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        # look for root in inorder list
        for i in range(len(inorder)):
            if inorder[i]==postorder[-1]: break
        left = self.buildTreeRecur(inorder[:i], postorder[:i])
        right = self.buildTreeRecur(inorder[i+1:], postorder[i:-1])
        if left is not None: root.left = left
        if right is not None: root.right = right
        return root

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = s.buildTree([2,1,3], [2,3,1])
    print root.val, root.left.val, root.right.val
    root = s.buildTree([1,2], [2,1])
    print root.val, root.left, root.right.val
