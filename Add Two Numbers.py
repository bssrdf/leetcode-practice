class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0; dummy = ListNode(-1); current = dummy
        while l1 is not None or l2 is not None or carry!=0:
            value = 0
            if l1: value+=l1.val
            if l2: value+=l2.val
            value+=carry
            value, carry = value%10, value/10
            current.next=ListNode(value)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

if __name__ == "__main__":
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    r = s.addTwoNumbers(l1, l2)
    while r!=None:
        print r.val,
        r = r.next