class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(x):
            if 2 <= x < 4:
                return True
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
                
            return True
            
        max_num = max(nums)
        prime_list = []
        for i in range(2, max_num):
            if is_prime(i):
                prime_list.append(i)
        
        res = 0
        for num in nums:
            for prime in prime_list:
                if prime >= int(num ** 0.5) + 1:
                    break
                if num % prime == 0:
                    a_div = int(num/prime)
                    if (a_div in prime_list or a_div == prime**2) and a_div != prime:
                        res += (1 + num + prime + a_div)
                    break
        return res
