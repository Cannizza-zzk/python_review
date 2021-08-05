class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, cnt = float('-inf'), 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end: 
                end = e
            else: 
                cnt += 1
        return cnt

# reference:https://leetcode.com/problems/non-overlapping-intervals/discuss/276056/Python-Greedy-Interval-Scheduling


""" class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #print(len(intervals))
        def has_overlap(start_i, end_i, start_j, end_j):
            if end_i > start_j and end_i < end_j:
                return True
            elif end_j > start_i and end_j < end_i:
                return True
            elif end_j == end_i and start_i == start_j:
                return True
            else:
                return False
        cnt , dif_intervals = 0 , []
        for i in range(len(intervals)):
            if intervals[i] not in dif_intervals:
                dif_intervals.append(intervals[i])
            else:
                cnt += 1
        
        overlap_dict = {}
        for i in range(len(dif_intervals)):
            for j in range(i):
                if has_overlap(dif_intervals[i][0],dif_intervals[i][1],dif_intervals[j][0],dif_intervals[j][1]):
                    if i in overlap_dict:
                        overlap_dict[i].append(j)
                    else:
                        overlap_dict[i] = [j]
                    if j in overlap_dict:
                        overlap_dict[j].append(i)
                    else:
                        overlap_dict[j] = [i]

        # print(overlap_dict)
        # print(cnt)
        while len(overlap_dict) != 0:
            # print(overlap_dict)
            cnt += 1
            i = max(overlap_dict, key=lambda k: len(overlap_dict[k]))
            list_i = overlap_dict[i]
           
            for item in list_i:
                overlap_dict[item].remove(i)
                if overlap_dict[item] == []:
                    del overlap_dict[item]
            del overlap_dict[i]

        return cnt


 """