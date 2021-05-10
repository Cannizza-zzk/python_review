class Solution:
    def __init__(self):
        self.cur_path = []
        self.ansRcd = []

    def dfs(self, cur_node:int,graph):
        # add current node to path
        self.cur_path.append(cur_node)
        # visit target node
        if cur_node == len(graph) - 1:
            self.ansRcd.append(self.cur_path.copy())
            self.cur_path.pop()
            return
        
        # traverse all possible next node
        for i in graph[cur_node]:
            self.dfs(i, graph)
        
        self.cur_path.pop()
        return


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.dfs(0, graph)
        return self.ansRcd