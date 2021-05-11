class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums,reverse=True)
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = sorted_nums[i/2]
            else:
                nums[i] = sorted_nums[len(nums)//2 + i//2]
        