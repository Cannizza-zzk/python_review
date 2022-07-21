class Solution:
    from collections import Counter
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        char_cnt = Counter(nums)
        for n_1, cnt in char_cnt.items():
            char_cnt[n_1] = cnt - 1
            for n_2, cnt_2 in char_cnt.items():
                if cnt_2 == 0 or n_2 < n_1: continue
                #print(n_1,n_2)
                char_cnt[n_2] = cnt_2 -1
                n_3 = 0 - n_1 - n_2
                if char_cnt[n_3] > 0 and n_3 >= n_2:
                    res.append([n_1,n_2,n_3])
                    
                char_cnt[n_2] = cnt_2 
            char_cnt[n_1] = cnt
        return res