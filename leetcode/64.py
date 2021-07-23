class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[i][j] means smallest sum from start to (i,j)
        dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]

        def find_path(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            if i > 0 and j > 0:
                dp[i][j] = min(find_path(i-1, j), find_path(i,j-1)) + grid[i][j]
            elif i > 0:
                dp[i][j] = find_path(i-1, j) + grid[i][j]
            elif j > 0:
                dp[i][j] = find_path(i, j-1) + grid[i][j]
            
            return dp[i][j]

        m , n = len(grid) , len(grid[0])
        find_path(m-1, n -1)
        return dp[-1][-1]