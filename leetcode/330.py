class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        upperbound = 1
        add_cnt = 0
        i = 0
        while upperbound <= n:
            if i < len(nums) and nums[i] <= upperbound:
                upperbound += nums[i]
                i += 1
            else:
                upperbound += upperbound
                add_cnt += 1

        return add_cnt


# reference: https://leetcode.com/problems/patching-array/discuss/78488/Solution-%2B-explanation