class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # abs(dp[i]) means the longest wiggle sequence ended with nums[i]
        # if dp[i] > 0 next difference should < 0 
        # else next difference should > 0 
        # dp[i] = max(abs(dp[n]) + 1)
        dp = [None for _ in range(len(nums))]

        dp[0] = 1 
        for i in range(1,len(dp)):
            for j in range(i):
                # dp[n] == 1 means nums[n] is a start of a subsequence so next can be either positive or negative
                if dp[j] == 1:
                    if nums[i] == nums[j]:
                        dp[i] = 1
                        continue
                    else:
                        if dp[i] == None or dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            dp[i] = -1 * dp[i] if nums[i] > nums[j] else dp[i]
                else:
                    if nums[i] == nums[j]:
                        dp[i] = 1 if dp[i] == None else dp[i]
                        continue
                    else:
                        if dp[i] == None and dp[j] * (nums[i] - nums[j]) > 0:
                            dp[i] = abs(dp[j]) + 1 if dp[j] < 0 else -1*(abs(dp[j]) + 1)
                        elif dp[i] != None and dp[j] * (nums[i] - nums[j]) > 0 and abs(dp[i]) < abs(dp[j])+1:
                            dp[i] = abs(dp[j]) + 1
                            dp[i] = -1 * dp[i] if dp[j] > 0 else dp[i]
        abs_dp = [abs(i) for i in dp]
        return max(abs_dp)

                    

