# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param preorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        root = self.buildTreeRecur(inorder, preorder)
        return root

    def buildTreeRecur(self, inorder, preorder):
        if len(inorder) == 0: return None
        if len(inorder) == 1: return TreeNode(inorder[0])
        root = TreeNode(preorder[0])
        # look for root in inorder list
        for i in range(len(inorder)):
            if inorder[i]==preorder[0]: break
        left = self.buildTreeRecur(inorder[:i], preorder[1:i+1])
        right = self.buildTreeRecur(inorder[i+1:], preorder[i+1:])
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
    root = s.buildTree([1,3,2,4], [1,2,3,4])
    print root.val