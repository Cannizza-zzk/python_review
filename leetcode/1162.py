class Solution:
    def distance(self,x0,y0,x1,y1):
        return abs(x0-x1) + abs(y0-y1)

    def maxDistance(self, grid: List[List[int]]) -> int:
        def is_valid(x,y):
            if x >= 0 and x < len(grid):
                if y >= 0 and y < len(grid[0]):
                    return True
            return False

        def bfs(i,j):
            for dist in range(1,len(grid)+len(grid[0])+1):
                for dx in range(dist +  1):
                    dy = dist - dx
                    if is_valid(i+dx,j+dy) and grid[i+dx][j+dy] == 1:
                        return dist
                    if is_valid(i-dx,j+dy) and grid[i-dx][j+dy] == 1:
                        return dist
                    if is_valid(i+dx,j-dy) and grid[i+dx][j-dy] == 1:
                        return dist
                    if is_valid(i-dx,j-dy) and grid[i-dx][j-dy] == 1:
                        return dist

            return -1
        res = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    continue
                res = max(res,bfs(i,j))
                if res == -1:
                    return res

        return res