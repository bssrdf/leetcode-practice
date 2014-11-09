class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        current = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
                current = current.next
                current.next = None
            else:
                current.next = l2
                l2 = l2.next
                current = current.next
                current.next = None
        if l1 is not None: current.next = l1
        if l2 is not None: current.next = l2
        return dummy.next

if __name__ == "__main__":
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    a1, a2, a3 = ListNode(1), ListNode(3), ListNode(5)
    a1.next, a2.next = a2, a3
    b1, b2, b3 = ListNode(2), ListNode(4), ListNode(6)
    b1.next, b2.next = b2, b3
    s = Solution()
    r = s.mergeTwoLists(a1, b1)
    while r:
        print r.val,
        r = r.next