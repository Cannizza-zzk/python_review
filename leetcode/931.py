class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp[i][j] means minimum falling path ended with matrix[i][j]
        # dp[i][j] = min(dp[i-1][j],dp[i-1][j-1], dp[i-1][j+1])

        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix[0])):
            dp[0][i] = matrix[0][i]

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                dp[i][j] = min(dp[i-1][j], dp[i-1][min(j+1, len(matrix[0])-1)], dp[i-1][max(0,j-1)]) + matrix[i][j]

        return min(dp[-1])