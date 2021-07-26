class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m , n = len(triangle) , len(triangle[-1])
        dp = [[None for _ in range(n)] for _ in range(m)]
        
        # dp[i][j] means minimum path sum to jth num in ith row
        # easily get: dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        dp[0][0] = triangle[0][0]
        def find_path(i , j):
            # basic
            if dp[i][j] != None:
                return dp[i][j]
            if j != 0:
                dp[i][j] = min(find_path(i-1,j), find_path(i-1,j-1)) + triangle[i][j] if j <= i-1 else find_path(i-1,j-1) +triangle[i][j]
            else:
                dp[i][j] = find_path(i-1,j) + triangle[i][j]
            return dp[i][j]

        for j in range(n):
            find_path(m-1,j)

        return min(dp[m-1])


