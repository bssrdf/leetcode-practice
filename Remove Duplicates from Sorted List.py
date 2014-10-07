# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None: return head
        current = head.next; prev = head
        while current is not None:
            if current.val == prev.val:
                prev.next = current.next
                current = prev.next
            else:
                prev = current
                current = current.next
        return head

if __name__ == "__main__":
    s = Solution()
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    p = s.deleteDuplicates(head)
    while p is not None:
        print p.val,
        p = p.next

