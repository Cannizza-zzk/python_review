class Solution:
    def twoEggDrop(self, n: int) -> int:
        i = 1
        while True:
            i += 1
            if sum([j for j in range(i)]) >= n:
                return i - 1

                