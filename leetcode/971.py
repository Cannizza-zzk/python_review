# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.voyage_remain = []
        self.flag = False
    def traversal(self, root: TreeNode):
        if self.flag: return
        if root == None or len(self.voyage_remain) == 0: return
        if root.val == self.voyage_remain[0]:
            self.voyage_remain.pop(0)
            if root.left != None and root.left.val != self.voyage_remain[0]:
                self.ans.append(root.val)
                tmp = root.left
                root.left = root.right
                root.right = tmp
            self.traversal(root.left)
            self.traversal(root.right)
        else:
            self.flag = True
            self.ans = [-1]
        

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.voyage_remain = voyage
        self.traversal(root)

        return self.ans
