class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # dp[i][j] contains an array with four elements
        # four elements means largest distance to four directions from center (i,j)
        # so order (i,j) sign = min(dp[i][j])
        # direction: dp[i][j][0] - up, ...[1] - down, ...[2] - left, ...[3] - right

        dp = [[[-1, -1, -1, -1] for _ in range(n)] for _ in range(n)]

        for mine in mines:
            dp[mine[0]][mine[1]] = [0, 0, 0, 0]

        maxOrder = 0

        for i in range(n):
            for j in range(n):
                if dp[i][j] == [0, 0, 0, 0]:
                    continue

                dp[i][j][0] = 1 if i == 0 else dp[i-1][j][0] + 1
                dp[i][j][2] = 1 if j == 0 else dp[i][j-1][2] + 1

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if dp[i][j] == [0, 0, 0, 0]:
                    continue
                
                dp[i][j][1] = 1 if i == n - 1 else dp[i + 1][j][1] + 1
                dp[i][j][3] = 1 if j == n - 1 else dp[i][j+1][3] + 1

                SignOrder = min(dp[i][j])
                maxOrder = max(SignOrder, maxOrder)

        return maxOrder

# O(2*n^2)