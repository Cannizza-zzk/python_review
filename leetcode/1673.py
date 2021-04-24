class Solution:

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st_arr = []
        
        for i in range(0,len(nums)):
            while len(st_arr) != 0 and st_arr[-1] > nums[i] and len(st_arr) + len(nums) - i - 1 >= k:
                st_arr.pop()
            if len(st_arr) < k:
                st_arr.append(num[i])        

        return st_arr
# reference: lee215 https://leetcode.com/problems/find-the-most-competitive-subsequence/discuss/952786/JavaC%2B%2BPython-One-Pass-Stack-Solution
'''
original code:
class Solution:

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st_arr = []
        for i in range(0,k):
            st_arr.append(nums[i])
        
        for i in range(k,len(nums)):
            st_arr.append(nums[i])
            for j in range(0,len(st_arr)-1):
                if st_arr[j] > st_arr[j+1]:
                    st_arr.pop(j)
                    break
            if len(st_arr) != k:
                st_arr.pop()

        return st_arr
'''
# passed cases:85/88