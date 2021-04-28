class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        cnt = 0
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        for col in range(0,len(grid)):
            for raw in range(0,len(grid[0])):
                cnt += 4 * grid[raw][col] + 2 if grid[raw][col] != 0 else 0
                for i in range(0,4):
                    if raw+dx[i] >=len(grid[0]) or raw+dx[i] < 0 or col+dy[i]<0 or col+dy[i]>=len(grid):
                        continue
                    else:
                        cnt -= grid[raw+dx[i]][col+dy[i]] if grid[raw+dx[i]][col+dy[i]] < grid[raw][col] else grid[raw][col]
                    
        return cnt
                    

                