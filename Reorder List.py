class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        # find middle point
        # reverse second half
        # join two halves
        if head is None or head.next is None: return head
        fast = head; slow = head
        dummy1 = ListNode(-1); dummy1.next = head; prev = dummy1
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next
        # middle starts from slow
        prev.next = None
        dummy2 = ListNode(-1); dummy2.next = slow
        current = slow
        while current.next is not None:
            temp = current.next
            current.next = current.next.next
            temp.next = dummy2.next
            dummy2.next = temp
        head1 = head; head2 = dummy2.next; current = dummy1
        while head1 is not None or head2 is not None:
            if head1 is not None:
                current.next= head1
                head1 = head1.next
                current = current.next
                current.next = None
            if head2 is not None:
                current.next = head2
                head2 = head2.next
                current = current.next
                current.next = None 
        return dummy1.next

if __name__ == "__main__":
    s = Solution()
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    dummy = ListNode(-1)
    curr = dummy
    for i in range(1, 20):
        curr.next = ListNode(i)
        curr = curr.next
    curr = dummy.next   
    while curr:
        print curr.val,
        curr = curr.next
    print "\r"
    res = s.reorderList(dummy.next)
    while res:
        print res.val,
        res = res.next
        