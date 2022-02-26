from heapq import heapify, heappop, heappush


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-v for v in piles]
        heapify(heap)
        for i in range(k):
            pile = -1 * heappop(heap)
            pile = pile - pile // 2
            heappush(heap, -1 * pile)

        return -1 * sum(heap)
