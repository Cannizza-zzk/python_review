class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        x, y = target
        d = abs(x) + abs(y)
        return all(d < abs(x - i) + abs(y - j) for i, j in ghosts)

# reference：https://leetcode.com/problems/escape-the-ghosts/discuss/116522/C%2B%2BJavaPython-Easy-and-Concise-Solution