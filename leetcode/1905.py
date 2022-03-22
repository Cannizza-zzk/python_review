class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n and grid2[i][j] == 1): return 1
            grid2[i][j] = 0
            res = grid1[i][j]
            for dx, dy in [[1,0], [0,1],[-1,0],[0,-1]]:
                res = res & dfs(i + dx, j + dy)
            return res
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j]:
                    cnt += dfs(i,j)
        return cnt




#reference: https://leetcode.com/problems/count-sub-islands/discuss/1284319/JavaC%2B%2BPython-DFS-Solution
# TLE
""" class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m , n = len(grid1), len(grid1[0])
        island1 = [[0 for _ in range(n)] for _ in range(m)]
        island2 = [[0 for _ in range(n)] for _ in range(m)]
        dx , dy = [1, 0, -1, 0], [0, 1, 0, -1]
        island_idx = 1

        def is_valid(x, y):
            if x >= 0 and x < m:
                if y >= 0 and y < n:
                    return True
            return False


        for i in range(m):
            for j in range(n):
                if island1[i][j] != 0: continue
                if grid1[i][j] != 0:
                    grid_queue = [[i,j]]
                    while len(grid_queue) != 0:
                        cur_i, cur_j = grid_queue.pop(0)
                        island1[cur_i][cur_j] = island_idx
                        for di, dj in zip(dx, dy):
                            if is_valid(cur_i + di, cur_j + dj) and island1[cur_i + di][cur_j + dj] == 0 and grid1[cur_i + di][cur_j + dj] == 1:
                                grid_queue.append([cur_i + di, cur_j + dj])

                    island_idx += 1
        cnt = 0
        for i in range(m):
            for j in range(n):
                if island2[i][j] != 0: continue
                if grid2[i][j] != 0:
                    flag = True
                    island_idx = island1[i][j]
                    if island_idx == 0: continue
                    grid_queue = [[i,j]]
                    while len(grid_queue) != 0:
                        cur_i, cur_j = grid_queue.pop(0)
                        island2[cur_i][cur_j] = 1
                        if island1[cur_i][cur_j] != island_idx:
                            flag = False
                        for di, dj in zip(dx, dy):
                            if is_valid(cur_i + di, cur_j + dj) and island2[cur_i + di][cur_j + dj] == 0 and grid2[cur_i + di][cur_j + dj] == 1:
                                grid_queue.append([cur_i + di, cur_j + dj])
                    if flag: cnt += 1

        return cnt """