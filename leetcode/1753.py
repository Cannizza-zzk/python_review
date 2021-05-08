class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int: 
        score = 0
        while (a != 0 and b != 0) or (c != 0 and b != 0) or (a != 0 and c != 0):
            score += 1
            if c <= a and c <= b:
                a -= 1
                b -= 1
            elif a <= b and a <= c:
                b -= 1
                c -= 1
            elif b <= a and b <= c:
                a -= 1
                c -= 1

        return score 

# greedy AC






# BFS timelimited passed 11/96
""" class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:  
        state_queue = []
        state_queue.append((a,b,c,0))
        max_Score = -1
        while len(state_queue) != 0:
            state_now = state_queue.pop(0)
            max_Score = state_now[3] if state_now[3] > max_Score else max_Score
            # add new node to queue
            if state_now[0] != 0 and state_now[1] != 0:
                state_queue.append((state_now[0]-1,state_now[1]-1,state_now[2],state_now[3]+1))
            if state_now[1] != 0 and state_now[2] != 0:
                state_queue.append((state_now[0],state_now[1]-1,state_now[2]-1,state_now[3]+1))
            if state_now[0] != 0 and state_now[2] != 0:
                state_queue.append((state_now[0]-1,state_now[1],state_now[2]-1,state_now[3]+1))

        return max_Score """
            

