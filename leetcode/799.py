class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # pour all champagne in
        dp = [[0 for _ in range(query_row + 2)] for _ in range(query_row + 2)]

        dp[0][0] = poured
        for row in range(1 , query_row + 2):
            for col in range(row + 1):
                if col == 0:
                    dp[row][col] = (dp[row - 1][col] - 1) / 2 if dp[row - 1][col] > 1 else 0
                    
                elif col == row:
                    dp[row][col] = (dp[row - 1][col - 1] - 1) / 2 if dp[row - 1][col - 1] > 1 else 0
                else:
                    dp[row][col] += (dp[row-1][col-1] - 1) / 2 if dp[row - 1][col - 1] > 1 else 0
                    dp[row][col] += (dp[row - 1][col] - 1) / 2 if dp[row - 1][col] > 1 else 0
                if col > 0:
                    dp[row-1][col-1] = min(1 , dp[row-1][col-1])

        return dp[query_row][query_glass]