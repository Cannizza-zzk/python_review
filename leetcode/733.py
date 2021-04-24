class Solution: 

    def floodFill(self,image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def is_valid(x,y,max_x,max_y):
            if x >= 0 and y >= 0:
                if x < max_x and y < max_y:
                    return True
            return False
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        max_x = len(image)
        max_y = len(image[0])
        OldColor = image[sr][sc]
        queue = []
        visited = {}
        queue.append([sr,sc])

        while len(queue) != 0:
            x = queue[0][0]
            y = queue[0][1]

            for i in range(0,4):
                if is_valid(x+dx[i],y+dy[i],max_x,max_y):
                    if visited.get((x+dx[i],y+dy[i])) != True:
                        if image[x+dx[i]][y+dy[i]] == OldColor:
                            queue.append([x+dx[i],y+dy[i]])
                            

            image[x][y] = newColor
            visited[(x,y)] = True
            queue.pop(0)
        return image

# bfs 
