class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        if n > 1: dp[0][1] = 1
        if m > 1: dp[1][0] = 1
        
        def find_path(i , j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            # update
            if i > 0 and j > 0:
                dp[i][j] = find_path(i-1,j) + find_path(i,j-1)
            elif i > 0:
                dp[i][j] = find_path(i-1, j)
            else:
                dp[i][j] = find_path(i,j-1)
            return dp[i][j]
        
        return find_path(m-1, n-1)
        