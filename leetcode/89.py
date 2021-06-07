class Solution:
    def __init__(self) -> None:
        self.path = []
        self.valid_choice = set()
        self.n = 0
    
    def valid_differ(self,a,b):
        a_bin = bin(a)[2:].zfill(self.n)
        b_bin = bin(b)[2:].zfill(self.n)
        cnt = 0
        for i in range(len(a_bin)):
            if a_bin[i] != b_bin[i]:
                cnt += 1
            if cnt == 2:
                return False
        if cnt == 1: return True
        else: return False

    def get_next(self, state_now, upperbound):
        for i in range(15,-1,-1):
            next_poss = 1 << i ^ state_now
            if next_poss in self.valid_choice and next_poss < upperbound:
                return next_poss
            
        return -1

    def grayCode(self, n: int) -> List[int]:
        for i in range(1,2**n):
            self.valid_choice.add(i)

        self.path.append(0)
        tmp = 2**n
        
        while True:
            if len(self.path) == 2**n and self.valid_differ(self.path[0],self.path[-1]):
                return self.path
            elif len(self.path) == 2**n:
                tmp = self.path.pop()
                self.valid_choice.add(tmp)
            
            next_state = self.get_next(self.path[-1], tmp)
            if next_state == -1:
                tmp = self.path.pop()
                self.valid_choice.add(tmp)
            else:
                self.path.append(next_state)
                self.valid_choice.remove(next_state)
            



