class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head is None: return None
        if head.next is None: return TreeNode(head.val)
        dummy = ListNode(-1); dummy.next = head
        fast, slow, prev = head, head, dummy
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next
        prev.next = None
        root = TreeNode(slow.val)
        left = self.sortedListToBST(head)
        right = self.sortedListToBST(slow.next)
        root.left = left
        root.right = right
        return root

if __name__ == "__main__":
    s = Solution()
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    head = ListNode(-1)
    dummy = head
    for i in range(7):
        head.next = ListNode(i+1)
        head = head.next
    res = s.sortedListToBST(dummy.next)
    print res.val