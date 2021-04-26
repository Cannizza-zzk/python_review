class Solution:
    def minFlips(self, target: str) -> int:
        seg_cnt = 0
        tail_seg = False
        for i in range(0,len(target) - 1):
            if target[i] == '1' and target[i+1] == '0':
                seg_cnt += 1
            
        if target[-1] == '1':
            tail_seg = True
        
        ans = 2*seg_cnt + 1 if tail_seg else 2*seg_cnt

        return ans