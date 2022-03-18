class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        min_r = float('inf')
        l , r = -1, -1
        for i in range(n-1, -1, -1):
            if arr[i] > min_r:
                l = i
                break
            min_r = min(min_r, arr[i])

        if l == -1: return arr
        max_r = 0
        for i in range(l+1, n):
            if arr[i] < arr[l]:
                r = i if arr[i] > max_r else r
                max_r = max(arr[i], max_r)
        arr[l], arr[r] =  arr[r], arr[l]
        return arr
