class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        dp[-1] = 0
        end = len(nums) - 1
        def min_step(i):
            # stored
            if dp[i] != -1:
                return dp[i]
            
            # basic
            if i + nums[i] >= end:
                dp[i] = 1
                return dp[i]
            
            for k in range(i+1, i + nums[i] + 1):
                step_k = min_step(k)
                if step_k != -1:
                    dp[i] = min(dp[i], step_k + 1) if dp[i] != -1 else step_k + 1

            return dp[i]

        min_step(0)
        #print(dp)
        return dp[0]
