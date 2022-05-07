class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def have_ol(interval1, interval2):
            s1, e1 = interval1
            s2, e2 = interval2
            if s2 <= s1 <= e2 or s1 <= s2 <= e1:
                return True
            else:
                return False
        res = [[0,0]]
        f = True
        ns, ne = newInterval
        if not intervals: return [newInterval]
        for i, interval in enumerate(intervals):
            if not have_ol(interval, newInterval) and f:
                res.append(interval)
            elif not have_ol(interval, newInterval) and not f:
                f = True
                res.append(interval)
            else:
                ns = min(interval[0],ns)
                ne = max(ne,interval[1])
                f = False
        res.append([float('inf'), float('inf')])
        
        for i in range(len(res)):
            if ns >= res[i][0] and ns < res[i+1][0]:
                res.insert(i+1, [ns,ne])
                break
      
        res.pop(-1)
        res.pop(0)
        return res
            


