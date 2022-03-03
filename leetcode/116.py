"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None: return root
        bfs_stack = [(root, 1)]

        while len(bfs_stack) != 0 :
            node, color = bfs_stack.pop(0)

            if node.left: bfs_stack.append((node.left, -1 * color))
            if node.right: bfs_stack.append((node.right, -1 * color))

            if len(bfs_stack) == 0 or bfs_stack[0][1] * color < 0:
                node.next = None
            else:
                node.next = bfs_stack[0][0]
        return root