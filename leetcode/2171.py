class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        sorted_b = [0] + sorted(beans)
        pre_sum = [0]
        for b in sorted_b:
            pre_sum.append(pre_sum[-1] + b)

        sum_b = pre_sum[-1]
        res = 0
        for i in range(1, len(sorted_b)):
            if sorted_b[i] != sorted_b[i-1]:
                threshold = sorted_b[i]
                l = len(sorted_b) - i
                res = min(res, sum_b - threshold*l) if res != 0 else sum_b - threshold*l

        return int(res)

