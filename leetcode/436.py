class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        res, idx_dict = [-1] * n, {}
        for idx, val in enumerate(intervals):
            idx_dict[val[0]] = idx

        intervals.sort(key = lambda x : x[0])

        for idx , interval in enumerate(intervals):
            start , end = interval[0] , interval[1]
            l , r = idx, n - 1
            if end > intervals[r][0]: continue

            while r >= l:
                mid = (r + l) // 2
                if mid == 0:
                    if intervals[mid][0] >= end: 
                        res[idx_dict[start]] = idx_dict[intervals[mid][0]]
                        break
                    else: l = mid + 1
                else:
                    if intervals[mid][0] >= end and intervals[mid - 1][0] < end:
                        res[idx_dict[start]] = idx_dict[intervals[mid][0]]
                        break
                    elif intervals[mid][0] < end:
                        l = mid + 1
                    else:
                        r = mid - 1

        return res



