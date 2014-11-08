class Solution:
    # @param head, a ListNode
    # @return a ListNode
    # merge sort
    def sortList(self, head):
        if head is None or head.next is None: return head
        slow = head; fast = head; prev = head
        while fast is not None and fast.next is not None:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None
        head1 = self.sortList(head)
        head2 = self.sortList(slow)
        res = self.merge(head1, head2)
        return res

    def merge(self, head1, head2):
        dummy = ListNode(-1); current = dummy
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                current.next = head1
                head1 = head1.next
                current = current.next
            else:
                current.next = head2
                head2 = head2.next
                current = current.next
        if head1 is not None: current.next = head1
        if head2 is not None: current.next = head2
        return dummy.next

if __name__ == "__main__":
    s = Solution()
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    head = ListNode(20)
    current = head
    for i in reversed(range(10)):
        current.next = ListNode(i)
        current = current.next
    current = head
    while current is not None:
        print current.val,
        current = current.next
    print "\r"
    res = s.sortList(head)
    current = res
    while current is not None:
        print current.val,
        current = current.next