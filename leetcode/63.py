class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m , n = len(obstacleGrid[0]) , len(obstacleGrid)
        # padding
        for row in obstacleGrid:
            row.append(1)
            row.insert(0,1)
        row_length = len(obstacleGrid[0])
        obstacleGrid.append([1]*row_length)
        obstacleGrid.insert(0,[1]*row_length)

        # dp[i][j] means num of path from start to (i , j)
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        dp[1][1] = 1 * (1 ^ obstacleGrid[1][1])

        def find_path(i , j):
            #print(i,j)
            if dp[i][j] != -1:
                return dp[i][j]
            
            # update
            if i > 1 and j > 1:
                dp[i][j] = find_path(i-1,j)  + find_path(i,j-1)
            elif i > 1:
                dp[i][j] = find_path(i-1, j) 
            elif j > 1:
                dp[i][j] = find_path(i,j-1) 
            dp[i][j] *= (1 ^ obstacleGrid[i][j])
            return dp[i][j]
        
        return find_path(n,m)