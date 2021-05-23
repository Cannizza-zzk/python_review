class Solution:
    def is_valid(self, gene:str, mutation:str):
        cnt = 0
        for i in range(len(gene)):
            if gene[i] != mutation[i]:
                cnt += 1
        if cnt == 1: return True
        else: return False

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        visited = [0] * len(bank)
        path_len = [0] * len(bank)
        state_queue = [start]
        minMut = -1
        while len(state_queue) != 0:
            # visit state now
            state_now = state_queue.pop(0)
            if state_now in bank:
                visited[bank.index(state_now)] = 1
            if state_now == end:
                if state_now == start: minMut = 0
                else: minMut = path_len[bank.index(state_now)]
                break
            
            # add new state to queue
            for i in range(len(bank)):
                if visited[i] != 0 and self.is_valid(state_now,bank[i]):
                    state_queue.append(bank[i])
                    path_len[i] = 1 if state_now == start else path_len[bank.index(state_now)] + 1
            
        return minMut
            
# BFS solution