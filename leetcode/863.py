# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_rcd = {}
        node_queue = [root]
        parent_rcd[root] = None
        start = None
        while len(node_queue) != 0:
            node_now = node_queue.pop(0)
            if node_now == target:
                start = node_now
            if node_now.left != None:
                parent_rcd[node_now.left] = node_now
                node_queue.append(node_now.left)
            if node_now.right != None:
                parent_rcd[node_now.right] = node_now
                node_queue.append(node_now.right)
        
        node_queue = [start]
        visited = {}
        path = {}
        path[start] = 0
        ans = []
        while len(node_queue) != 0:
            node_now = node_queue.pop(0)
            if path[node_now] == k:
                ans.append(node_now.val)
            visited[node_now.val] = True
            if node_now.left != None and node_now.left.val not in visited:
                node_queue.append(node_now.left)
                path[node_now.left] = path[node_now] + 1
            if node_now.right != None and node_now.right.val not in visited:
                node_queue.append(node_now.right)
                path[node_now.right] = path[node_now] + 1
            if parent_rcd[node_now] != None and parent_rcd[node_now].val not in visited:
                node_queue.append(parent_rcd[node_now])
                path[parent_rcd[node_now]] = path[node_now] + 1

        return ans
            



