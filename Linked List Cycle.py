class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast = head; slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow: return True
        return False

if __name__ == "__main__":
    s = Solution()
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    print s.hasCycle(head)

