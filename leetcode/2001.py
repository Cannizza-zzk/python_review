import math


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        def C_n_2(n):
            upper = math.factorial(n)
            lower = math.factorial(2) * math.factorial(n-2)
            return upper/ lower

        rec_cnt = {}
        for w, h in rectangles:
            ratio = float(w) / float(h)
            if ratio in rec_cnt.keys():
                rec_cnt[ratio] += 1
            else:
                rec_cnt[ratio] = 1
            
        ans  = 0
        for k, v in rec_cnt.items():
            if v >= 2:
                ans += C_n_2(v)
        return int(ans)