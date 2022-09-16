class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m , n = len(a) , len(b)
        # condition 3
        ch_a = Counter(ord(c) - 97 for c in a)
        ch_b = Counter(ord(c) - 97 for c in b)

        res = m + n - max((ch_a + ch_b).values())

        for i in range(25):
            ch_a[i + 1] += ch_a[i]
            ch_b[i + 1] += ch_b[i]

            res = min(res, ch_b[i] + m - ch_a[i])
            res = min(res, ch_a[i] + n - ch_b[i])

        return res


# reference: https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/discuss/1032070/JavaC%2B%2BPython-Clean-Solution