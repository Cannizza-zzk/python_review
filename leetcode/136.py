class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        for i in range(0, len(sorted_nums),2):
            if i == len(sorted_nums) - 1:
                return sorted_nums[i]
            if sorted_nums[i] != sorted_nums[i+1]:
                return sorted_nums[i]