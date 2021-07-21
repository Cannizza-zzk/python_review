class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [False for _ in range(len(nums))]
        can_reach[0] = True
        index_queue = [0]
        farest = 0
        
        while len(index_queue) != 0:
            index_now = index_queue.pop(0)
            can_reach[index_now] = True
            farest = max(farest, index_now + nums[index_now], len(nums))
            for k in range(index_queue[-1] + 1, farest + 1):
                index_queue.append(k)
                
        return can_reach[-1]    
        