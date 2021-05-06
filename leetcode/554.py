class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        change_rcd = {}
        for i in range(len(wall)):
            change_point = 0
            for j in range(len(wall[i])-1):
                change_point += wall[i][j]
                if change_rcd.get(change_point) == None:
                    change_rcd[change_point] = 1
                else:
                    change_rcd[change_point] += 1
            
        min_cnt = len(wall)
        for key,value in change_rcd.items():
            cnt = len(wall) - value
            if cnt < min_cnt:
                min_cnt = cnt
        
        return min_cnt

# inspired by https://leetcode.com/problems/brick-wall/discuss/888577/IntuitionC%2B%2BWith-PicturesHashMapDetailed-ExplanationCommentsSolutionCode

# original code passed 85/87 cases
# time limited
""" class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        start = 0
        end = sum(wall[0])
        dp = []
        change = set()
        if len(wall) == 1:
            if len(wall[0]) == 1:
                return 1
            else: return 0
        for i in range(len(wall)):
            dp.append([])
            change_point = 0
            for j in range(len(wall[i])):
                change_point += wall[i][j]
                dp[i].append(change_point)
                #print(dp)
                change.add(change_point)
        #print(dp)
        change.remove(end)
        min_cnt = len(wall)
        for point in change:
            cnt = 0
            # count brick
            for i in range(len(wall)):
                for j in range(len(wall[i])):
                    if point < dp[i][j]:
                        cnt += 1
                        break
                    if point == dp[i][j]:
                        break
                
            if cnt < min_cnt:
                min_cnt = cnt
        
        return min_cnt """
        

