class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.rcd = []
    def search_targ(self, candidates, targ, state_now):
        if len(candidates) == 0: return
        if sum(candidates) < targ: return
        if candidates[0] == targ:
            state_now.append(candidates[0])
            cnt_arr = collections.Counter(state_now)
            flag = True
            for cnt in self.rcd:
                #print(cnt.most_common,cnt_arr.most_common)
                if cnt == cnt_arr : 
                    flag = False
                    #print('turn false')
            if flag:
                #print(self.rcd)
                #print(state_now)
                self.ans.append(state_now.copy())
                self.rcd.append(cnt_arr)
            state_now.pop()
            self.search_targ(candidates[1:],targ,state_now)
        elif candidates[0] > targ:
            self.search_targ(candidates[1:],targ,state_now)
        elif candidates[0] < targ:
            state_now.append(candidates[0])
            self.search_targ(candidates[1:],targ - candidates[0],state_now)
            state_now.pop()
            self.search_targ(candidates[1:],targ,state_now)
        return


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.search_targ(candidates,target,[])
        return self.ans