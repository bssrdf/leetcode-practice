class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m==n: return head
        dummy = ListNode(-1); dummy.next = head
        prev = dummy; current = head; cnt = 1
        while cnt!= m:
            current = current.next
            prev = prev.next
            cnt+=1
        while cnt <= n-1:
            temp = current.next
            current.next = current.next.next
            temp.next = prev.next
            prev.next = temp
            cnt+=1
        return dummy.next

if __name__ == "__main__":
    s = Solution()
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    nodes = []
    for i in range(9):
        nodes.append(ListNode(i+1))
    for i in range(8):
        nodes[i].next = nodes[i+1]
    head = nodes[0]
    while head is not None:
        print head.val,
        head = head.next
    print '\r'
    head = s.reverseBetween(nodes[0], 4, 6)
    while head is not None:
        print head.val,
        head = head.next
    print '\r'
    head = s.reverseBetween(nodes[0], 1, 6)
    while head is not None:
        print head.val,
        head = head.next
    print '\r'


