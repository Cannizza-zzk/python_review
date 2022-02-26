# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        l_tree, r_tree = [], []
        if len(preorder) == 0:
            return None
        tree_root = TreeNode(val = preorder[0])
        root_val = preorder.pop(0)
        for v in preorder:
            if v < root_val:
                l_tree.append(v)
            else:
                r_tree.append(v)

        tree_root.left = self.bstFromPreorder(l_tree)
        tree_root.right = self.bstFromPreorder(r_tree)

        return tree_root