# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head.next is None and n == 1: return None
        fast = head; slow = head
        dummy = ListNode(-1); dummy.next = head
        prev = dummy
        for i in range(n):
            fast = fast.next
        while fast is not None:
            fast = fast.next; slow = slow.next; prev = prev.next
        prev.next = slow.next
        return dummy.next

if __name__ == "__main__":
    s = Solution()
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    head = ListNode(1)
    p = head
    for i in range(2, 6):
        p.next = ListNode(i)
        p = p.next
    p = s.removeNthFromEnd(head, 5)
    while p is not None:
        print p.val,
        p = p.next


