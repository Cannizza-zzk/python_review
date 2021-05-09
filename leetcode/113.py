#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.hisPath = []
        self.ans = []
    
    def dfs(self,cur_node:TreeNode, SumNow:int, targetSumL:int):
        # visit current node
        if cur_node == None:
            return
        else:
            self.hisPath.append(cur_node.val)
        # current node is leaf
        if cur_node.left == None and cur_node.right == None:
            if cur_node.val + SumNow == targetSumL:
                self.ans.append(self.hisPath.copy())
                return
            else:
                return
        # current node is not leaf
       
        if cur_node.left != None:
            self.dfs(cur_node.left, SumNow + cur_node.val, targetSumL)
            self.hisPath.pop()
        if cur_node.right != None:
            self.dfs(cur_node.right, SumNow + cur_node.val, targetSumL)
            self.hisPath.pop()

        return

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.dfs(root, 0, targetSum)
        return self.ans