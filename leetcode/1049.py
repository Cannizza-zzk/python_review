class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumStones = 0
        for stone in stones:
            sumStones += stone

        dp = [[-1 for _ in range(sumStones // 2 + 1)] for _ in range(len(stones))]

        def find_max(i,j):
            if dp[i][j] != -1:
                return dp[i][j]

            if i == 0:
                if stones[i] <= j:
                    dp[i][j] = stones[i]
                else:
                    dp[i][j] = 0
                return dp[i][j]

            dp[i][j] = find_max(i-1, j)
            if j - stones[i] >= 0:
                dp[i][j] = max(dp[i][j], find_max(i-1,j-stones[i]) + stones[i])

            return dp[i][j]
        
        res = find_max(len(stones)-1,sumStones // 2)      
        
        return (sumStones - res) - res

# reference: https://leetcode.com/problems/last-stone-weight-ii/discuss/672906/Explanation%3A-Why-Problem-is-Knapsack
# DP step: 1.寻找解空间 2.定义状态 3.计算状态