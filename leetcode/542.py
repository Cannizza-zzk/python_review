class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # dp[i][j] means distance of nearest 0 to mat[i][j]
        # dp[i][j] = 0 if mat[i][j] == 0 else min(dp[i+1][j],dp[i][j+1],dp[i-1][j],dp[i][j-1]) + 1
        m , n = len(mat) , len(mat[0])
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        q = []
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def is_valid(i,j):
            if i < 0 or j < 0:
                return False
            if i > m - 1 or j > n - 1:
                return False
            return True
                
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append([i,j])
        
        while len(q) != 0:
            row , col  = q.pop(0)
            for k in range(4):
                next_row = row + dx[k]
                next_col = col + dy[k]

                if is_valid(next_row,next_col) and ans[next_row][next_col] == -1:
                    ans[next_row][next_col] = ans[row][col] + 1
                    q.append([next_row,next_col])

    
        return ans
