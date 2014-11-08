class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None: return head
        dummy = ListNode(-1)
        first = head; second = head.next; current = dummy
        while first is not None and second is not None:
            first.next = second.next
            second.next = first
            current.next = second
            first = first.next
            current = current.next.next
            if first is not None: 
                second = first.next
            else: second = None
        return dummy.next

if __name__ =="__main__":
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    s =Solution()
    head = ListNode(1)
    head.next=ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    res = s.swapPairs(head)
    while res!=None:
        print res.val,
        res = res.next
    print ""

