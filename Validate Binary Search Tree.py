class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBSTRecur(root, -9223372036854775808, 9223372036854775807)

    def isValidBSTRecur(self, root, minnode, maxnode):
        if root is None: return True
        if root.val>minnode and root.val<maxnode: isRoot = True
        else: isRoot = False 
        isLeft = self.isValidBSTRecur(root.left, minnode, root.val)
        isRight = self.isValidBSTRecur(root.right, root.val, maxnode)
        return isRoot and isLeft and isRight

if __name__ == "__main__":
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    s = Solution()
    t1, t2, t3, t4, t5 = TreeNode(1), TreeNode(0), TreeNode(3), TreeNode(4), TreeNode(5)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t4.right = t5
    print s.isValidBST(t1)