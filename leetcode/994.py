class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 2D -> 1D: grid[m][n] = index 100*m + n
        # BFS

        q, f = [], []
        d = [1,-1,100,-100]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([100*i+j,0])
                if grid[i][j] == 1:
                    f.append(100*i+j)

        res = 0
        while q:
            idx, time = q.pop(0)
            for delta in d:
                if idx + delta in f:
                    q.append([idx + delta, time + 1])
                    f.remove(idx+delta)
                    res = max(res, time+1)
                
        if not f:
            return res
        else:
            return -1
        