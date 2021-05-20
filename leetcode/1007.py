class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        num_rcd = collections.Counter(tops + bottoms)
        targ = -1
        tops_cnt , bottoms_cnt = 0 , 0
        ans = -1
        for num, times in num_rcd.items():
            if times >= len(tops):
                targ = num
                break
        
        if targ == -1:
            return ans

        for i in range(len(tops)):
            if tops[i] != targ and bottoms[i] != targ:
                return ans
            if tops[i] == targ and bottoms[i] == targ:
                continue  
            elif tops[i] == targ:
                tops_cnt += 1
            elif bottoms[i] == targ:
                bottoms_cnt += 1
            
        ans = bottoms_cnt if bottoms_cnt < tops_cnt else tops_cnt
        return ans
        
