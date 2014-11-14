# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None: return None
        visited = {}
        current = [node]
        while len(current)!=0:
            next = []
            for curr in current:
                new_node = UndirectedGraphNode(curr.label)
                visited[curr] = new_node
                for neighbor in curr.neighbors:
                    if neighbor not in visited:
                        next.append(neighbor)
            current = next
        for each in visited:
            for neighbor in each.neighbors:
                visited[each].neighbors.append(visited[neighbor])
        return visited[node]

if __name__ == "__main__":
    s = Solution()
    class UndirectedGraphNode:
        def __init__(self, x):
            self.label = x
            self.neighbors = []
    node0 = UndirectedGraphNode(0)
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node0.neighbors.append(node1)
    node0.neighbors.append(node2)
    node1.neighbors.append(node2)
    node2.neighbors.append(node2)
    res = s.cloneGraph(node0)
    print res.label




