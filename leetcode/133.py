"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        node_queue = [node]
        new_node_dict = {}

        while len(node_queue) != 0:
            # visit first
            node_now = node_queue.pop(0)
            if node_now.val not in new_node_dict:
                new_node = Node(node_now.val, None)
                new_node_dict[node_now.val] = new_node

            # add new
            for neighbor in node_now.neighbors:
                if neighbor.val not in new_node_dict:
                    node_queue.append(neighbor)
                    new_node = Node(neighbor.val, None)
                    new_node_dict[neighbor.val] = new_node
                new_node_dict[node_now.val].neighbors.append(new_node_dict[neighbor.val])
                

        return new_node_dict[node.val]


# bfs solution