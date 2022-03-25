from heapq import heapify, heappop


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        heapify(nums)
        res,  last = 0, 0
        while nums:
            num = heappop(nums)
            #print(num, k)
            if num != last and num != last + 1 and k != 0:
                if num - last - 1 > k:
                    res += int((last + 1 + last + k)*k/2)
                    k = 0
                else:
                    res += int((last + num) * (num - last - 1) / 2)
                    k -= (num - last - 1)
            res += num
            last = num
        if k != 0:
            res += int((last + 1 + last + k) * k / 2)
        return res - s