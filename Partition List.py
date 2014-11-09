class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        dummy_small = ListNode(-1)
        dummy_large = ListNode(-1)
        current = head
        current_small = dummy_small
        current_large = dummy_large
        while current is not None:
            if current.val < x:
                current_small.next = current
                current = current.next
                current_small = current_small.next
                current_small.next = None
            else:
                current_large.next = current
                current = current.next
                current_large = current_large.next
                current_large.next = None
        current_small.next = dummy_large.next
        return dummy_small.next
     
if __name__ == "__main__":
    s = Solution()
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    node1, node2, node3, node4, node5, node6 = ListNode(1), ListNode(4), ListNode(3), ListNode(2), ListNode(5), ListNode(2)
    node1.next, node2.next, node3.next, node4.next, node5.next = node2, node3, node4, node5, node6
    res = s.partition(node1, 3)
    while res is not None:
        print res.val,
        res = res.next
    print "\r"

