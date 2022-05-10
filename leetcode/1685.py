class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        p, res = [0], []
        for num in nums:
            p.append(p[-1] + num)
        
        for i in range(len(nums)):
            pre_len, past_len = i, len(nums) - i - 1
            res_i = 0
            res_i += p[-1] - p[i + 1] - past_len * nums[i]
            res_i += pre_len * nums[i] - p[i] 
            res.append(res_i)
        return res