class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digit_dict = collections.Counter(str(n))
        for i in xrange(30):
            if digit_dict == collections.Counter(str(1<<i)):
                return True
            
        return False

        
