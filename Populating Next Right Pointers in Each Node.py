class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None: return
        current = [root]
        while len(current)!=0:
            next = []
            for i in range(len(current)):
                if current[i].left: next.append(current[i].left)
                if current[i].right: next.append(current[i].right)
                if i!=len(current)-1:
                    current[i].next = current[i+1]
            current = next

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
            self.next = None
    node1, node2, node3 = TreeNode(1), TreeNode(2), TreeNode(3)
    node1.left = node2
    node1.right = node3
    s.connect(node1)
    print node2.next.val
