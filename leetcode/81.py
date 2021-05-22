class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start_idx = 0
        
        for i in range(len(nums)-1):                
            if nums[i] > nums[i + 1]:
                start_idx = i + 1
                break
        
        originList = nums[start_idx:] + nums[:start_idx]
        if target < originList[0] or target > originList[-1]: return False
        start, end = 0 , len(nums) - 1
        while start <= end:
            if start == end:
                if target == originList[start]: return True
                else: return False
            mid = (start + end) // 2
            if target == originList[start] or target == originList[mid] or target == originList[end]:
                return True
            elif target > originList[mid]:
                start = mid if start != mid else start + 1
            elif target <originList[mid]:
                end = mid
            
            
        return False
            

