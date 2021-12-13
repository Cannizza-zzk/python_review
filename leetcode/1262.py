class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # a number % 3 = 0 or 1 or 2
        import math

        total_sum = sum(nums)

        remain = {0:[], 1:[], 2:[]}
        for num in nums:
            if num % 3 == 0:
                remain[0].append(num)
            elif num % 3 == 1:
                remain[1].append(num)
            else:
                remain[2].append(num)

        if total_sum % 3 == 0:
            return total_sum
        elif total_sum % 3 == 1:
            prob1 = math.inf if len(remain[1]) == 0 else min(remain[1])
            if len(remain[2]) < 2:
                prob2 = math.inf
            else:
                prob2 = min(remain[2])
                remain[2].remove(prob2)
                prob2 += min(remain[2])

            if prob2 == math.inf and prob1 == math.inf:
                return 0
            else:
                return total_sum - min(prob1,prob2)
        else:
            prob1 = math.inf if len(remain[2]) == 0 else min(remain[2])
            if len(remain[1]) < 2:
                prob2 = math.inf
            else:
                prob2 = min(remain[1])
                remain[1].remove(prob2)
                prob2 += min(remain[1])

            if prob2 == math.inf and prob1 == math.inf:
                return 0
            else:
                return total_sum - min(prob1,prob2)