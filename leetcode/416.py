class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Array_sum = sum(nums)
        if Array_sum % 2 != 0:
            return False
        
        # dp[i] means i can be sum of a subarray 
        # dp[i] = dp[i - num_0] or dp[i - num_1] ... or dp[i - num_n] for num in nums
        dp = {}
        mask = [1 for _ in range(len(nums))]
        def canForm(i):
            if i in dp:
                return dp[i]
            
            if i < 0:
                return False
            elif i == 0:
                return True
            
            for index, num in enumerate(nums):
                if mask[index] == 0:
                    continue
                mask[index] = 0
                if canForm(i - num):
                    dp[i] = True
                    return dp[i]
                mask[index] = 1
            dp[i] = False
            return dp[i]
        return canForm(Array_sum//2)
