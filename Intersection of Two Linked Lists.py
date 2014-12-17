# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA, lenB = 0, 0; curA, curB = headA, headB
        while curA is not None:
            lenA+=1
            curA=curA.next
        while curB is not None:
            lenB+=1
            curB=curB.next
        curA, curB = headA, headB
        if lenA>lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        if lenB>lenA:
            for i in range(lenB-lenA):
                curB = curB.next
        while curA!=curB:
            curA=curA.next
            curB=curB.next
        return curA

if __name__ == "__main__":
    s=Solution()
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node3; node1.next.next = node4; node2.next = node4
    res = s.getIntersectionNode(node1, node2)
    print res.val