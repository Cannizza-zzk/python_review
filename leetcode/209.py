class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        pre_sum = [0, nums[0]]
        for i in range(1, len(nums)):
            pre_sum.append(nums[i] + pre_sum[-1])

        l, r = 0, 1
        res = float('inf')
        while l != len(nums):
            if pre_sum[r] - pre_sum[l] >= target:
                res = min(res, r - l)
                l += 1
            else:
                if r == len(nums):
                    l = len(nums)
                else:
                    r += 1
        return int(res) 
