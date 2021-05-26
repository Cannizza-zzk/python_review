class Solution:
    def numTeams(self, rating: List[int]) -> int:
        lless_rcd = {}
        rless_rcd = {}
        lgreater_rcd = {}
        rgreater_rcd = {}
        for i in range(len(rating)):
            lless_rcd[i] = 0
            lgreater_rcd[i] = 0
            rless_rcd[i] = 0
            rgreater_rcd[i] = 0

        for i in range(len(rating)):
            for pre_ptr in range(i):
                if rating[pre_ptr] < rating[i]:
                    lless_rcd[i] += 1
                elif rating[pre_ptr] > rating[i]:
                    lgreater_rcd[i] += 1
            for back_ptr in range(i+1, len(rating)):
                if rating[back_ptr] < rating[i]:
                    rless_rcd[i] += 1
                elif rating[back_ptr] > rating[i]:
                    rgreater_rcd[i] += 1
                    
        ans = 0
        for i in range(len(rating)):
            ans += lless_rcd[i] * rgreater_rcd[i] + lgreater_rcd[i] * rless_rcd[i]
        return ans


# reference: https://leetcode.com/problems/count-number-of-teams/discuss/554795/C%2B%2BJava-O(n-*-n)-and-O(n-log-n)

# DFS Solution time limite exceeded
#57 / 72 test cases passed
""" 
class Solution:
    def __init__(self) -> None:
        self.ans = 0
    def dfs(self, lower_bound, listRemain, numRemain):
        if numRemain == 0:
            self.ans += 1
            return
        if len(listRemain) < numRemain:
            return
        
        if listRemain[0] > lower_bound:
            self.dfs(listRemain[0], listRemain[1:],numRemain-1)
        
        self.dfs(lower_bound,listRemain,numRemain)
        return

    def numTeams(self, rating: List[int]) -> int:
        self.dfs(-1, rating, 3)
        rating.reverse()
        self.dfs(-1, rating, 3)
        return self.ans """
        