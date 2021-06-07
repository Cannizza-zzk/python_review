class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        dp = [0] * (len(nums) + 1)
        hash_map = {}
        for idx, num in enumerate(nums):
            dp[idx] = num if idx == 0 else dp[idx-1] + num
        for idx, num in enumerate(dp):
            hash_map[num] = idx
        hash_map[0] = -1

        targ = dp[-1] - x
        #print(targ)
        sum = 0
        maxLen = -1
        for i in range(len(nums)):
            sum += nums[i]
            if sum - targ in hash_map:
                maxLen = max(maxLen, i - hash_map[sum - targ])
        if maxLen == -1: return -1
        return len(nums) - maxLen

        # reference : https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/935935/Java-Detailed-Explanation-O(N)-Prefix-SumMap-Longest-Target-Sub-Array