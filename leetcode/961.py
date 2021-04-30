class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        apperance_dict = {}
        for i in range(0,len(A)):
            if apperance_dict.get(A[i]) == None:
                apperance_dict[A[i]] = True
            else:
                return A[i]