class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0: return None
        if len(num) == 1: return TreeNode(num[0])
        mid = len(num)/2
        root = TreeNode(num[mid])
        left = self.sortedArrayToBST(num[:mid])
        right = self.sortedArrayToBST(num[mid+1:])
        root.left = left; root.right = right
        return root

if __name__ == "__main__":
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    s = Solution()
    print s.sortedArrayToBST([1,2,3]).val