class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] means length of LIS end with nums[i]
        # dp[i] = dp[i - n] + 1 (nums[i-n] is nearst one which is smaller than nums[i])

        dp = [1 for _ in range(len(nums))]

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i] , dp[j] + 1)
        
        return max(dp)

# classic