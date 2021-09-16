class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp[i] means LIS ended with nums[i]
        # dp[i] = max(dp[k] | where nums[k] < nums[i]) + 1
        # O(n^2)
        n = len(nums)
        dp = [1 for _ in range(n)]
        cnt = [1 for _ in range(n)]
       

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        cnt[i] = 0
                    dp[i] = max(dp[i],dp[j] + 1)
                    if dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]

        ans = 0
        for index, length in enumerate(dp):
            if length == max(dp):
                ans += cnt[index]
        return ans