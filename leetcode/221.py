class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        res = 0
        def find_max(x,y):
            max_square = 0
            pqueue = [[x,y]]
            while len(pqueue) != 0:
                point = pqueue.pop(0)
                if point[0] >= len(matrix) or point[1] >= len(matrix[0]):
                    break
                if matrix[point[0]][point[1]] == '1':
                    if point[0] - x == point[1] - y:
                        max_square += 1
                        pqueue.append([point[0],point[1]+1])
                        pqueue.append([point[0]+1,point[1]])
                        pqueue.append([point[0]+1,point[1]+1])
                    elif point[0] - x > point[1] - y:
                        pqueue.append([point[0]+1,point[1]])
                    else:
                        pqueue.append([point[0],point[1]+1])
                else:
                    return max_square 
            return max_square


        for i in range(len(matrix)):
            if res >= len(matrix) - i:
                break
            for j in range(len(matrix[0])):
                if res >= len(matrix[0]) - j:
                    break
                res = max(find_max(i,j),res)

        return res*res