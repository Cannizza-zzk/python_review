class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cnt = 0
        path ,pre_record = [0] , {}
        for num in nums:
            path.append(path[-1] + num)
            pre_record[path[-1] + num] = 0

        for pre_sum in path:
            for targ in range(lower, upper+1):
                if pre_sum - targ in pre_record:
                    cnt += pre_record[pre_sum - targ]
            
            pre_record[pre_sum] += 1


        return cnt
# TLE passed:60/67