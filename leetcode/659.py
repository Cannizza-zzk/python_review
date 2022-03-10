
import collections
from email.policy import default


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # a num have two way to go:
        #   1. to the end of a subsequence 
        #   2. as the start of a new subsequence
        # if a number cannot be arranged two ways above return false

        left = collections.Counter(nums)
        end  = collections.defaultdict(int)

        for num in nums:
            if not left[num]: continue
            left[num] -= 1

            if end[num-1]:
                end[num] += 1
                end[num-1] -= 1
            elif left[num+1] and left[num+2]:
                end[num+2] += 1
                left[num+1] -= 1
                left[num+2] -= 1
            else:
                return False

        return True