# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.node_hightrcd = {}
    
    def find_hight(self, root: TreeNode):
        # leaf node
        if root.right == None and root.left == None:
            self.node_hightrcd[root] = 0
            return 0
        # inner node
        if root.right and root.left:
            rhight = self.find_hight(root.right)
            lhight = self.find_hight(root.left)
            self.node_hightrcd[root] = rhight + 1 if rhight >= lhight else lhight + 1
        elif root.right:
            rhight = self.find_hight(root.right)
            self.node_hightrcd[root] = rhight + 1
        elif root.left:
            lhight = self.find_hight(root.left)
            self.node_hightrcd[root] = lhight + 1

        return self.node_hightrcd[root]
        
    def find_ans(self, root: TreeNode):
        if root == None: return None
        if root.left == None and root.right == None:
            return root
        elif root.left == None:
            return self.find_ans(root.right)
        elif root.right == None:
            return self.find_ans(root.left)
            
        if self.node_hightrcd[root.left] == self.node_hightrcd[root.right]:
            return root
        if self.node_hightrcd[root.left] > self.node_hightrcd[root.right]:
            return self.find_ans(root.left)
        else:
            return self.find_ans(root.right)

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.find_hight(root)
        return self.find_ans(root)

