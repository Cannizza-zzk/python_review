class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # min(right) >= max(left)
        # left_dp[i] store max(nums[0:i+1])
        # right_dp[i] store min(nums[i:])

        l = len(nums)
        right_dp, left_dp = [0] * l, [0] * l
        left_dp[0] , right_dp[-1] = nums[0], nums[-1]
        for i in range(1 , l):
            left_dp[i] = max(nums[i], left_dp[i-1])
            right_dp[-(i+1)] = min(nums[-(i+1)], right_dp[-i])
            
        for i in range(l):
            if right_dp[i+1] >= left_dp[i]:
                return i + 1