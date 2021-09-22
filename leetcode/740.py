class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # dp[i] means most points can get if earn i | where i in elem in nums
        # dp[i] = i * i_num + max(dp[i-2], dp[i-3])
        from collections import Counter
        num_cnt = Counter(nums)
        max_n = max(nums)
        dp = [0 for _ in range(max(max_n + 1,3))]
        dp[0] , dp[1] , dp[2] = 0, num_cnt[1], num_cnt[2] * 2
        ans = max(dp)

        for i in range(3, max_n+1):
            #print(dp)
            dp[i] = i * num_cnt[i] + max(dp[i-2], dp[i-3])
            ans = max(ans,dp[i])

        return ans

            

