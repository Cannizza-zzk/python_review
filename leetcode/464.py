class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        state = ''
        for i in range(maxChoosableInteger+1):
            state += '1'
        state_rcd = {}

        def canWin(state_now, RemainTotal):
            if (state_now,RemainTotal) in state_rcd:
                return state_rcd[(state_now,RemainTotal)]
            
            sum_i = 0
            for i in range(len(state_now)-1,0,-1):
                sum_i += i
                if state_now[i] == '1' and i >= RemainTotal:
                    state_rcd[(state_now,RemainTotal)] = True
                    return state_rcd[(state_now,RemainTotal)]
            if sum_i < RemainTotal:
                state_rcd[(state_now,RemainTotal)] = False
                return state_rcd[(state_now,RemainTotal)]
            
            for i in range(1,len(state_now)):
                if state_now[i] == '1':
                    next_state = state_now[0:i] + '0' +state_now[i+1:]
                    if not canWin(next_state, RemainTotal - i):
                        state_rcd[(state_now,RemainTotal)] = True
                        return state_rcd[(state_now,RemainTotal)]
            state_rcd[(state_now,RemainTotal)] = False
            return state_rcd[(state_now,RemainTotal)]

        res = canWin(state, desiredTotal)
        #print(state_rcd)
        return res

# 状态压缩
# 最大可选数为n，则应当存在2^n个状态
# 若一个状态，存在一个下一状态，该下一状态为必败态，则该状态是必胜态
# gtmd