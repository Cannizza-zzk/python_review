class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ans = [-1] * len(quiet)
        richer_dict = {i :[i] for i in range(len(quiet))}
        for con in richer:
            richer_dict[con[1]].append(con[0])
        def find_ansi(i):
            if ans[i] >= 0: return ans[i] # basic case
            ans[i] = i
            for j in richer_dict[i]:
                if quiet[ans[i]] > quiet[find_ansi(j)]:
                    ans[i] = ans[j]
            return ans[i]
        for i in range(len(quiet)): find_ansi(i)
        return ans

# DFS solution
# reference : https://leetcode.com/problems/loud-and-rich/discuss/137918/C%2B%2BJavaPython-Concise-DFS



# BFS solution 
# timelimit exceeded
# 81 / 86 test cases passed.
""" class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richerDict = {i : [i] for i in range(len(quiet))}
        sorted_quiet = [(i,quiet[i]) for i in range(len(quiet))]
        sorted_quiet.sort(key= lambda x : x[1])
        for con in richer:
            richerDict[con[1]].append(con[0])
        
        ans = []
        for i in range(len(quiet)):
            bfs_queque = []
            bfs_queque += richerDict[i]
            richer_ones = set()
            richer_ones.update(elem for elem in bfs_queque)
            while len(bfs_queque) != 0:
                this_one = bfs_queque.pop(0)
                richer_ones.update(elem for elem in richerDict[this_one])
                for elem in richerDict[this_one]:
                    if elem not in bfs_queque and elem != this_one:
                        bfs_queque.append(elem)
            ans_i = i
            for i in range(len(sorted_quiet)):
                if sorted_quiet[i][0] in richer_ones:
                    ans_i = sorted_quiet[i][0]
                    break
            ans.append(ans_i)
        
        return ans """
                
                
