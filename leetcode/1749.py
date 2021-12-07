class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_pre , min_pre = 0 , 0
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            max_pre = max(pre_sum,max_pre)
            min_pre = min(pre_sum,min_pre)

        return abs(max_pre-min_pre)



#reference:https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/discuss/1052527/JavaC%2B%2BPython-O(1)-Space
# TLE solution
""" class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur , res = set(), set()
        for num in nums:
            cur = {num + i for i in cur} | {num}
            res = res | cur

        return max(abs(max(res)),abs(min(res))) """