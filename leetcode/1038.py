# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.pre_sum = {}
        path = []
        def traverse_tree(root, visit):
            if root.left != None:
                traverse_tree(root.left, visit)

            visit(root)

            if root.right != None:
                traverse_tree(root.right, visit)
            return 

        def get_sum(root):
            self.pre_sum[root.val] = self.sum
            self.sum += root.val
            return
        def reval(root):
            root.val = self.sum - self.pre_sum[root.val]
            return
        traverse_tree(root, get_sum)
        traverse_tree(root,reval)
        return root

# better right to left
# reference:https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/discuss/286725/JavaC%2B%2BPython-Revered-Inorder-Traversal
      

        

            