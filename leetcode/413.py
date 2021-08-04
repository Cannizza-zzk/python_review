class Solution:
    def cal_nums(self,start, end):
        #print(start,end)
        length = end - start + 1
        if length < 3:
            return 0
        
        cnt = 0
        for i in range(3, length + 1):
            cnt += length - i + 1

        return cnt
        

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        p_back , p_pre = 0 , 1
        cnt = 0
        if len(nums) <= 1:
            return 0
        diff = nums[1] - nums[0]

        while p_pre < len(nums):
            if diff != nums[p_pre] - nums[p_pre-1]:
                cnt += self.cal_nums(p_back,p_pre-1)
                p_back = p_pre - 1
                diff = nums[p_pre] - nums[p_pre-1]
            p_pre += 1
        
        
        cnt += self.cal_nums(p_back,p_pre - 1)

        return cnt