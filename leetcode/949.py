class Solution:     
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        res = collections.Counter(str(i) for i in arr)
        ans = ''
        for h in range(23,-1,-1):
            for m in range(59,-1,-1):
                if h < 10 and h != 0:
                    timenum = str(h * 1000 + m)
                elif h == 0 and m == 0:
                    timenum = '0000'
                else:
                    timenum = str(h * 100 + m)
                #print(timenum)
                if res == collections.Counter(timenum):
                    ans = '%02d' % h
                    ans += ':'
                    ans += '%02d' % m
                    return ans
        return ans