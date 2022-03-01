from heapq import heapify, heappop


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs_heap = costs
        heapify(costs_heap)

        cnt = 0
        while costs_heap:
            cnt += 1
            a = heappop(costs_heap)
            coins -= a
            if coins < 0:
                return cnt - 1

        return cnt