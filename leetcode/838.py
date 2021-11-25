class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        right_distance = [0]* len(dominoes)
        left_distance = [0]* len(dominoes)

        for i in range(1, len(dominoes)):
            if dominoes[i] == '.' and dominoes[i-1] == 'R':
                right_distance[i] = 1
            if dominoes[i] == '.' and right_distance[i-1] != 0:
                right_distance[i] = right_distance[i-1] + 1
        
        for i in range(len(dominoes) - 2, -1, -1):
            if dominoes[i] == '.' and dominoes[i+1] == 'L':
                left_distance[i] = 1
            if dominoes[i] == '.' and left_distance[i+1] != 0:
                left_distance[i] = left_distance[i+1] + 1

        for i in range(len(dominoes)):
            if left_distance[i] != 0 and right_distance[i] != 0:
                if left_distance[i] == right_distance[i]:
                    dominoes[i] = '.'
                else:
                    dominoes[i] = 'R' if right_distance[i] < left_distance[i] else 'L'
            elif left_distance[i] == 0 and right_distance[i] != 0:
                dominoes[i] = 'R' if dominoes[i] == '.' else dominoes[i]
            elif left_distance[i] != 0 and right_distance[i] == 0:
                dominoes[i] = 'L' if dominoes[i] == '.' else dominoes[i]
           

        return ''.join(dominoes)
                
# reference: https://leetcode.com/problems/push-dominoes/discuss/1352339/C%2B%2B-Simple-and-Clean-Easy-to-Understand-O(n)-Solution-With-detailed-Explanation