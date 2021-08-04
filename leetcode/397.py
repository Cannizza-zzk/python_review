class Solution:
    def integerReplacement(self, n: int) -> int:
        # dp[i] means number of operations needed for i to 1
        # i is even: dp[i] = 1 + dp[i/2]
        # i is odd: dp[i] = 1 + min(dp[i-1],dp[i+1])
        dp = {}
        dp[1] = 0
        
        def min_operation(i):
            if i in dp:
                return dp[i]
            
            if i % 2 == 0:
                dp[i] = 1 + min_operation(i // 2)
            else:
                dp[i] = 1 + min(min_operation(i - 1), min_operation(i + 1))

            return dp[i]

        return min_operation(n)