class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        num_sum = sum(nums)
        if num_sum % k != 0 or max(nums) > num_sum // k:
            return False
        targ = num_sum // k

        buckets = [targ for i in range(k)]

        def dfs(state, buckets):
            buckets.sort(reverse = True)
            if len(state) == 0:
                return True
            next_num = state.pop(0)
            if next_num > max(buckets):
                return False

            for index, cap in enumerate(buckets):
                if cap >= next_num:
                    buckets[index] -= next_num
                    if dfs(state.copy(), buckets.copy()):
                        return True
                    buckets[index] += next_num
            return False
        nums.sort(reverse=True)
        return dfs(nums, buckets)


