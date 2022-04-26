class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l ,r = 0, len(arr) - 1
        while l < r and arr[l] <= arr[l + 1]:
            l += 1
        if l == r: return 0
        while r > 0 and arr[r] >= arr[r-1]:
            r -= 1

        res = min(r,len(arr) - (l + 1))
        j = r
        for i in range(l+1):
            if arr[i] <= arr[j]:
                res = min(j - i - 1, res)
            elif j < len(arr) - 1:
                j += 1
            else:
                break
        return res