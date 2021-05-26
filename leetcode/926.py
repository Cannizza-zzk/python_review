class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # cnt_0/1 means the num of '0' behind position now and the num of '1' before the position now
        cnt_0 = s.count('0')
        cnt_1 = 0
        ans = len(s) - cnt_0
        for i in range(len(s)):
            if s[i] == '0':
                cnt_0 -= 1
            else:
                ans = min(ans, cnt_0 + cnt_1)
                cnt_1 += 1

        return ans
            





# reference: https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/184110/python-O(n)-time-O(1)-space-solution-with-explanation(with-extra-Chinese-explanation)

# BFS solution time limit exceeded
# 16 / 81 test cases passed
""" class Solution:
    def is_mono(self, s:str)-> bool:
        flag = True
        for i in range(len(s) - 1):
            if s[i] == '1' and s[i + 1] == '0':
                flag = False
        return flag

    def flip(self, s:str, pos:int)->str:
        sList= list(s)
        sList[pos] = '1' if s[pos] == '0' else '0'
        s = ''.join(sList)
        return s

    def minFlipsMonoIncr(self, s: str) -> int:
        state_queue =[(s, 0)]
        state_rcd = [s]
        while len(state_queue) != 0:
            state_now = state_queue.pop(0)
            if self.is_mono(state_now[0]):
                return state_now[1]
            for i in range(len(state_now[0])):
                next_state = self.flip(state_now[0],i)
                if next_state not in state_rcd:
                    state_queue.append((next_state,state_now[1]+1))
                    state_rcd.append(next_state) """
        
