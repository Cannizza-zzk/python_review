class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i][j] means max stones can be get from piles[i:j+1] by first player
        # dp[i][j] = max(sum(piles[i:j+1]) - dp[i+1][j], sum(piles[i:j+1]) - dp[i][j-1])
        # if dp[0][len(piles)-1] > sum(piles) // 2: return true
        
        dp = [[-1 for _ in range(len(piles))] for _ in range(len(piles))]

        def get_dp(i,j):
            if dp[i][j] != -1:
                return dp[i][j]

            if i == j:
                dp[i][j] = piles[i]
                return dp[i][j]

            totalStone = sum(piles[i:j+1])
            dp[i][j] = max(totalStone - get_dp(i+1,j),totalStone-get_dp(i,j-1))
            
            return dp[i][j]
        
        if get_dp(0,len(piles)-1) > sum(piles) //2:
            return True
        else:
            return False
