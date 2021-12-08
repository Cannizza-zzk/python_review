class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        from collections import Counter
        import math
        if not set(b) <= set(a):
            return -1
        
        a_cntr = Counter(a)
        ptr_a, ptr_b = 0 , 0
        start_num = a_cntr[b[0]]
        res = math.inf

        for i in range(start_num):
            ptr_a = a.index(b[0],ptr_a+1 if i != 0 else 0)
            ptra_cp = ptr_a
            ptr_b = 0
            rep_num = 1

            while True:
                if ptr_b == len(b):
                    res = min(res, rep_num)
                    break
                if ptr_a == len(a):
                    ptr_a = 0
                    rep_num += 1
                
                if a[ptr_a] != b[ptr_b]:
                    break
                else:
                    ptr_a += 1
                    ptr_b += 1
            ptr_a = ptra_cp

        return res if res != math.inf else -1
