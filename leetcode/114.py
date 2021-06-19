# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        treenodeList = []
        def pre_order(root):
            # visit node now
            treenodeList.append(root)
            # basic situation
            if root.left == None and root.right == None:
                return

            if root.left != None: pre_order(root.left)
            if root.right != None: pre_order(root.right)
            return 
        if root != None:
            pre_order(root)
        else:
            return
        for idx, node in enumerate(treenodeList):
            node.left = None
            node.right = treenodeList[idx+1] if idx < len(treenodeList) - 1 else None
        
        return
        
