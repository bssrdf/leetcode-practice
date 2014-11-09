class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or head.next is None: return head
        dummy = ListNode(-1); dummy.next = head
        current = head.next; prev = head
        while current is not None:
            if current.val>=prev.val:
                current = current.next
                prev = prev.next
            else:
                check = dummy.next; prev_check = dummy
                while check.val<=current.val:
                    check = check.next
                    prev_check = prev_check.next
                prev.next = current.next
                current.next = prev_check.next
                prev_check.next = current
                current = prev.next
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
    res = s.insertionSortList(head)
    current = res
    while current is not None:
        print current.val,
        current = current.next

