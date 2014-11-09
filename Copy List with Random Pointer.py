class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None: return None
        mp_new = {}; mp_old = {}; res = []; current = head
        while current is not None:
            new_node = RandomListNode(current.label)
            res.append(new_node)
            mp_new[new_node] = current
            mp_old[current] = new_node
            current = current.next
        for node in res:
            if mp_new[node].next: node.next = mp_old[mp_new[node].next]
            if mp_new[node].random: node.random = mp_old[mp_new[node].random]
        return res[0]

if __name__ == "__main__":
    s = Solution()
    class RandomListNode:
        def __init__(self, x):
            self.label = x
            self.next = None
            self.random = None
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.next.next = RandomListNode(3)
    head_copy = s.copyRandomList(head)
    while head_copy != None:
        print head_copy.label,
        head_copy = head_copy.next
    print "\r"
