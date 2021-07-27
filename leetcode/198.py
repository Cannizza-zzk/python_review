class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] means: if house i was the last one got robbed, the largest amount of money we get
        # easily: dp[i] = max(dp[i-2],dp[i-3]) + nums[i]
        # prove:
        # 1. house i-1 cannot be robbed if we rob dp[i] 
        # 2. dp[i-4] < dp[i-2] and dp[i-5] < dp[i-3] is a certain according to the formula
        #    clearly if we rob house i-5 and then house i, the money will less than rob house i-5,i-3,i 
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        dp = [-1 for _ in range(len(nums))]
        dp[0] , dp[1] , dp[2] = nums[0] , nums[1] , nums[2] + nums[0]
        def max_money(i):
            # basic
            if dp[i] != -1:
                return dp[i]

            dp[i] = max(max_money(i-2),max_money(i-3)) + nums[i]
            return dp[i]

        return max(max_money(len(nums)-1),max_money(len(nums)-2))

            

            

