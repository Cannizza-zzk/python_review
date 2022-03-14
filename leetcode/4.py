class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: 
            a , b, m, n = nums2, nums1, n, m
        else:
            a , b = nums1, nums2

        if m == 0:
            return (b[n//2] + b[n//2 - 1 + n%2])/2.0
        if n == 0:
            return (a[m//2] + a[m//2 - 1 + m%2])/2.0
        targ = (m + n) // 2 if (m + n) % 2 != 0 else (m + n) // 2 - 1

        l , r = 0, m
        while l < r:
            mid = (l + r) // 2
            if targ - mid - 1 < 0 or b[targ - mid - 1] <= a[mid]:
                r = mid
            else:
                l = mid + 1

        mid = r
        candi = sorted(a[mid:mid + 2] + b[targ-mid:targ-mid+2])
        if (m + n) %2 == 0:
            return (candi[0] + candi[1]) / 2.0
        else:
            return candi[0]


