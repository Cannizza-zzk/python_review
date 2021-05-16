from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        leftCost = [0] * len(boxes)
        rightCost = [0] * len(boxes)
        lcnt = int(boxes[0])
        rcnt = int(boxes[-1])
        for i in range(1,len(boxes)):
            for j in range(i,len(boxes)):
                leftCost[j] += lcnt
            lcnt += int(boxes[i])
        for i in range(len(boxes)-2,-1,-1):
            for j in range(i,-1,-1):
                rightCost[j] += rcnt
            rcnt += int(boxes[i])
        #print(leftCost)
        #print(rightCost)
        ans = []
        for i in range(len(leftCost)):
            ans.append(leftCost[i] + rightCost[i])

        return ans