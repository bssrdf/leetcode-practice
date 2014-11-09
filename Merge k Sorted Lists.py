import heapq

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        dummy = ListNode(-1)
        heap = []
        for ll in lists:
            if ll is not None:
                heapq.heappush(heap, (ll.val, ll))
        current = dummy
        while len(heap)>0:
            node = heapq.heappop(heap)[1]
            current.next = node
            current = current.next
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, node.next))
        return dummy.next

if __name__ == "__main__":
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    s = Solution()
    l1 = ListNode(4)
    l1.next = ListNode(6)
    l1.next.next = ListNode(11)
    l2 = ListNode(5)        
    l2.next = ListNode(7)
    l2.next.next = ListNode(9)
    l3 = ListNode(2)
    l3.next = ListNode(18)
    lists = [l1, l2, l3]
    res = s.mergeKLists(lists)
    while res != None:
        print res.val,
        res = res.next      
    print ""

