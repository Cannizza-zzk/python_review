class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        ans = [1]
        while len(ans) < n:
            ans = [2 * i -1 for i in ans] + [2 * i for i in ans]
        return [i for i in ans if i < n]

# reference : https://leetcode.com/problems/beautiful-array/discuss/186679/Odd-%2B-Even-Pattern-O(N)
# salute to lee215