def containsNearbyAlmostDuplicate(self, nums, k, t):
    if t < 0: return False
    n = len(nums)
    d = {}
    w = t + 1
    for i in xrange(n):
        m = nums[i] / w
        if m in d:
            return True
        if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
            return True
        if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
            return True
        d[m] = nums[i]
        if i >= k: del d[nums[i - k] / w]
    return False

# 30 / 30 test cases passed.
# Status: Accepted
# Runtime: 56 ms
# 93.81%
# reference:https://leetcode.com/problems/contains-duplicate-iii/discuss/61639/JavaPython-one-pass-solution-O(n)-time-O(n)-space-using-buckets