class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # fibseq need 2 elements to ensure the state
        # for example : we know first two elements or last two elements 
        # we can get the whole sequence

        maxLen = 0
        s = set(arr)

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                ijLen = 2
                a , b = arr[i], arr[j]
                while a + b in s:
                    a , b ,ijLen = b, a + b, ijLen+1
                if ijLen > 2:
                    maxLen = max(maxLen, ijLen)

        return maxLen

# search an element in set is far more faster than search in list
# reference: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/discuss/152343/C%2B%2BJavaPython-Check-Pair