class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head is None or head.next is None: return head
        dummy = ListNode(-1); dummy.next = head
        current = head; prev = dummy; cnt = 0
        while current is not None:
            cnt+=1
            if cnt%k==0:
                # return last element in reversed group
                prev = self.reverseList(prev, current.next)
                current = prev.next
            else:
                current = current.next
        return dummy.next

    def reverseList(self, prev, later):
        current = prev.next
        while current.next != later:
            temp = current.next
            current.next = current.next.next
            temp.next = prev.next
            prev.next = temp
        return current

if __name__ == "__main__":
    s = Solution()
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    input = []
    for i in range(7):
        input.append(ListNode(i+1))
    for i in range(6):
        input[i].next = input[i+1]
    head = input[0]
    curr = head
    while curr is not None:
        print curr.val,
        curr = curr.next
    print "\r"
    curr = s.reverseKGroup(head, 3)
    while curr is not None:
        print curr.val,
        curr = curr.next
    print "\r"        
