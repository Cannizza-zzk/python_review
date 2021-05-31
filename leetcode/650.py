class Solution:
    def is_prime(self, n):
        for i in range(int(pow(n,0.5)) + 1):
            if n % i == 0:
                return False
        return True

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        elif self.is_prime(n):
            return n
        else:
            for i in range(int(pow(n,0.5))+1):
                if n % i == 0:
                    return i + self.minSteps(n//i)
        