class Solution:
    def __init__(self) -> None:
        self.dp = [[[-1] * 101 for _ in range(26)] for _ in range(26)]
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0 : return 1
        dx = [1, -1, 2, -2, 1, -1, 2, -2]
        dy = [2, 2, 1, 1, -2, -2, -1, -1]
        ans = 0
        #print(row,column,k)
        if self.dp[row][column][k] != -1 :
            return self.dp[row][column][k]

        for i in range(len(dx)):
            if row + dx[i] >= 0 and row + dx[i] < n and column + dy[i] >= 0 and column + dy[i] < n:
                ans += 0.125 * self.knightProbability(n, k-1, row +dx[i], column + dy[i])

        self.dp[row][column][k] = ans
        return ans
        