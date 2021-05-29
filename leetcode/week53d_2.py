class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = -1
        for i in range(len(nums) / 2):
            if ans > 0:
                ans = min(ans, nums[i] + nums[-i-1])
            else:
                ans = nums[i] + nums[-1-i]

        return ans