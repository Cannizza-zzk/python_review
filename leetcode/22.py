class Solution:
    def __init__(self):
        self.left_stack = []
        self.right_stack = []
        self.ansStr = ''
        self.ansRcd = []
    def dfs(self):
        # basic 
        if len(self.left_stack) == 0 and len(self.right_stack) == 0:
            self.ansRcd.append(self.ansStr)
            return
        
        # select next element
        if len(self.left_stack) == len(self.right_stack):
            nextEle = self.left_stack.pop()
            self.ansStr = self.ansStr + nextEle
            self.dfs()
            self.ansStr = self.ansStr[:-1]
            self.left_stack.append('(')
        elif len(self.left_stack) == 0:
            num = len(self.right_stack)
            self.ansRcd.append(self.ansStr + num*')')
        else:
            nextEle = self.left_stack.pop()
            self.ansStr = self.ansStr + nextEle
            self.dfs()
            self.ansStr = self.ansStr[:-1]
            self.left_stack.append('(')

            nextEle = self.right_stack.pop()
            self.ansStr = self.ansStr + nextEle
            self.dfs()
            self.ansStr = self.ansStr[:-1]
            self.right_stack.append(')')
        return

    def generateParenthesis(self, n: int) -> List[str]:
        for i in range(n):
            self.left_stack.append('(')
            self.right_stack.append(')')
        self.dfs()
        return self.ansRcd
