class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] means the number of possible combination to get a target i
        # dp[i] = sum(dp[i-num]) for num in nums
        dp = [-1 for _ in range(target+1)]
        dp[0] = 1
        def count_combinations(targ):
            if targ < 0: return 0
            if dp[targ] != -1:
                return dp[targ]
            
            dp[targ] = 0
            for num in nums:
                dp[targ] += count_combinations(targ-num)

            return dp[targ]

        return count_combinations(target) 
            
