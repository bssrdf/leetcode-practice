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
        dummy = ListNode(-1)
        current = head.next; prev = head; prevprev = dummy
        while current is not None:
            if current.val == prev.val:
                current = current.next
            else:
                # only connect to dummy when ensuring prev has no duplicates
                if prev.next == current: 
                    prevprev.next = prev
                    prevprev = prev
                    prevprev.next = None
                    prev = current
                    current = current.next
                # jump over all old prev elements w/ duplicates
                # but still not sure whether new prev has duplicates
                else:
                    prev = current
                    current = current.next
        if prev.next is None: prevprev.next = prev
        return dummy.next

if __name__ == "__main__":
    s = Solution()
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(2)
    res = s.deleteDuplicates(head)
    while res is not None:
        print res.val,
        res = res.next
    print "\r"