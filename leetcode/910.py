class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        up_bnd, low_bnd = max(nums), min(nums)
        nums.sort()
        res = up_bnd - low_bnd
        for idx, num in enumerate(nums):
            if idx == len(nums) - 1: break
            up_bnd = max(nums[-1], num + 2*k)
            low_bnd = min(nums[idx + 1], nums[0] + 2*k)
            res = min(res, up_bnd - low_bnd)
        
        return res