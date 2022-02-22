from collections import defaultdict

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        garden_adj = defaultdict(list)
        for i, j in paths:
            garden_adj[i-1].append(j-1)
            garden_adj[j-1].append(i-1)

        ans = [None] * n

        # initial 
        ans[0] = 1
        
        for i in range(1, n):
            choice = [1, 2, 3, 4]
            for j in garden_adj[i]:
                if ans[j] != None and ans[j] in choice:
                    choice.remove(ans[j])
            ans[i] = choice[0]

        return ans
                    

        