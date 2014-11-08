class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None or head.next is None: return head
        current = head; i = 0
        while current is not None:
            i+=1
            current = current.next
        shift = k%i
        if shift == 0: return head
        dummy = ListNode(-1); dummy.next = head
        fast = head; slow = head; prev_slow = dummy; prev_fast = dummy
        for i in range(shift):
            fast, prev_fast = fast.next, prev_fast.next
        while fast is not None:
            slow, fast = slow.next, fast.next
            prev_fast, prev_slow = prev_fast.next, prev_slow.next
        prev_fast.next = head; prev_slow.next = None; dummy.next = slow
        return dummy.next

if __name__ == "__main__":
    s = Solution()
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    node1, node2, node3, node4, node5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
    head = s.rotateRight(node1, 2)    
    while head is not None:
        print head.val,
        head = head.next
    print "\r"


