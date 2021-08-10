class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[(i,j)] means number of ways to get amount j using coins[0:i+1]
        # dp[(i,j)] = sum(dp[i-1, j - n * coins[i]]| n*coins[i] < j)
        dp = {}
        
        def count_ways(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j == 0:
                return 1
            
            if i == 0:
                if j % coins[i] == 0:
                    dp[(i,j)] = 1
                    return dp[(i,j)]
                else:
                    dp[(i,j)] = 0
                    return dp[(i,j)]

            n , dp[(i,j)] = 0 , 0
            while True:
                if n * coins[i] > j:
                    break
                dp[(i,j)] += count_ways(i-1, j - n * coins[i])
                n += 1

            return dp[(i,j)]

        return count_ways(len(coins)-1, amount)
            
            
