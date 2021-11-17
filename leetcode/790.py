class Solution:
    def numTilings(self, n: int) -> int:
        # dp1[i] means number of tilling ways for 2 * i - 1 space
        # dp2[i] means number of tilling ways for 2 * i space
        # dp1[i] = dp2[i-2] + dp1[i-1]
        # dp2[i] = dp2[i-1] + dp2[i-2] + dp1[i-1] * 2 
        dp1 = [0 for _ in range(n+1)]
        dp2 = [0 for _ in range(n+1)]
        dp1[1] , dp1[0] = 0 , 0
        dp2[0] , dp2[1] = 1 , 1
        mod = int(1e9+7)
        
        for i in range(2, n+1):
            dp1[i] = dp2[i-2] + dp1[i-1]
            dp2[i] = dp2[i-1] + dp2[i-2] + dp1[i-1] * 2 

        return dp2[n]%mod


        # reference: https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116534/Python-Easy-and-Concise-Solution