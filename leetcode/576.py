class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # dp[i][j][k] means ball in grid [i,j] and has k times move to use, in this
        # situation, numbers of paths out boundary
        # easily, dp[i][j][k] = sum(dp[i+dx][j+dy][k-1])
        # specialy we define if i+dx,j+dy out of boundary, dp[i+dx][j+dy][k] = 1
        # if k = 0, dp[i][j][k] = 0
        dp = [[[-1 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for i in range(m):
            for j in range(n):
                dp[i][j][0] = 0

        def out_bound(i, j):
            if i < 0 or j < 0:
                return True
            if i >= m or j >= n:
                return True
            return False

        def cnt_path(i, j, k):
            if dp[i][j][k] != -1:
                return dp[i][j][k]

            cnt = 0
            for direction in range(4):
                ni = i + dx[direction]
                nj = j + dy[direction]
                if out_bound(ni,nj):
                    cnt += 1
                else:
                    cnt += cnt_path(ni,nj,k-1)

            dp[i][j][k] = cnt
            return dp[i][j][k]
            
        mod = 10**9 + 7

        return cnt_path(startRow,startColumn,maxMove) % mod