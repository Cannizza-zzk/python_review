class Solution:
    def minDays(self, A, m, k):
        if m * k > len(A): return -1
        left, right = 1, max(A)
        while left < right:
            mid = (left + right) / 2
            flow = bouq = 0
            for a in A:
                flow = 0 if a > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m: break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return left

# binary search
# reference：https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/686316/JavaC%2B%2BPython-Binary-Search










""" 

TLE


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n: return -1
        elif m*k == n: return max(bloomDay)

        from collections import Counter
        keyDay = Counter(bloomDay)

        f_num = 0
        
        for day, num in sorted(keyDay.items(), key = lambda item:item[0]):
            f_num += num
            if f_num < m*k: continue
                
            # print(day, num)

            bou_num, flow_num = m, k 
            for i in range(n):
                if bloomDay[i] > day:
                    flow_num = k 
                    continue
                else:
                    flow_num -= 1
                    if flow_num == 0:
                        bou_num -= 1
                        flow_num = k
                        if bou_num == 0:
                            return day 
                 """