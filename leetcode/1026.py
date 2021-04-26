# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode, max_val: int, min_val: int)-> int:
        # update
        max_val = max(max_val,root.val)
        min_val = min(min_val,root.val)
        if root.left == None and root.right == None:
            return abs(max_val - min_val)
        if root.left != None:
            left_diff = self.dfs(root.left,max_val,min_val)
        if root.right != None:
            right_diff = self.dfs(root.right,max_val,min_val)
        
        if root.left != None and root.right != None:
            ans = max(right_diff,left_diff)
        elif root.left == None:
            ans = right_diff 
        else:
            ans = left_diff 
        return ans

    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.dfs(root,root.val,root.val)
