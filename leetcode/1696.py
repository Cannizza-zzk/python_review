
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # dp[i] means max score when reach nums[i]
        # dp[i] = nums[i] + max(dp[i-k:i])
        length = len(nums)
        dp = [0] * length
        # initial 
        dp[0] = nums[0]
        dq = deque([[dp[0],0]])
        for i in range(1, length):
            dp[i] = nums[i] + dq[0][0]

            while dq and dq[-1][0] < dp[i]:
                dq.pop()
            dq.append([dp[i],i])
            if i - k == dq[0][1]:
                dq.popleft()
            

        return dp[-1]