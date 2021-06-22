class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def points_dis(point1, point2):
            dx = point1[0] - point2[0]
            dy = point1[1] - point2[1]
            sum_square = dx ** 2 + dy ** 2
            return pow(sum_square,0.5)
        dis_rcd = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = points_dis(points[i],points[j])
                if distance in dis_rcd:
                    dis_rcd[distance].append([i,j])
                else:
                    dis_rcd[distance] = [[i,j]]
            
        def find_top(ppList):
            topnumDict = {}
            for point_pair in ppList:
                if point_pair[0] in topnumDict:
                    topnumDict[point_pair[0]] += 1
                else:
                    topnumDict[point_pair[0]] = 1
                if point_pair[1] in topnumDict:
                    topnumDict[point_pair[1]] += 1
                else:
                    topnumDict[point_pair[1]] = 1

            topnumList = []
            for key, value in topnumDict.items():
                if value != 1:
                    topnumList.append([key,value])
            return topnumList
        
        def Cn2(n):
            return n*(n-1)/2
        ans = 0
        for dist, pairList in dis_rcd.items():
            topList = find_top(pairList)
            for pair in topList:
                ans += 2 * Cn2(pair[1])

        return int(ans)


        
        