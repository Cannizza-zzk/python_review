class Solution:
    def __init__(self) -> None:
        self.string = ''
        self.path = []
        self.flag = False

    def dfs(self, pos, divide_pt):
        # basic situation
       
        if divide_pt == 0 and pos == len(self.string) - 1:
            return
        if pos == len(self.string) - 1:
            if int(self.string[divide_pt:]) == self.path[-1] - 1:
                self.flag = True
            return
        
        #print(self.path)
        # divide
        if len(self.path) == 0 or int(self.string[divide_pt:pos+1]) == self.path[-1] - 1:
            self.path.append(int(self.string[divide_pt:pos+1]))
            self.dfs(pos + 1, pos + 1)
            self.path.pop()
            
        # nothing to do
        self.dfs(pos+1, divide_pt)

        return


    def splitString(self, s: str) -> bool:
        self.string = s
        self.dfs(0, 0)

        return self.flag


    def splitString(self, s: str) -> bool:
        self.string = s
        self.dfs(0, 0)

        return self.flag