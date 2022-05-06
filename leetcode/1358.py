class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pre_cnt = [[0,0,0]]

        for i in range(len(s)):
            pre_cnt.append(pre_cnt[i].copy())
            idx = int(ord(s[i]) - ord('a'))
            pre_cnt[i+1][idx] += 1

        res = 0
        for r in range(len(pre_cnt)):
            if 0 in pre_cnt[r]: continue
            for l in range(max(0, r - 2), -1, -1):
               sub_cnt = [m - n for m,n in zip(pre_cnt[r],pre_cnt[l])]
               if not (0 in sub_cnt):
                   res += l + 1
                   break

        return res
        




