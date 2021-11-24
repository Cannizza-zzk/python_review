class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # dp[n,k] means max score in nums[:n] with k subarray

        dp = {}

        def find_dp(n, k):
            if (n,k) in dp:
                return dp[(n,k)]

            if n < k: return 0

            if k == 1:
                dp[(n,k)] = sum(nums[:n]) / n
                return dp[(n,k)]

            tmp, dp[(n,k)] = 0 , 0
            for i in range(n-1, 0 , -1):
                tmp += nums[i]
                dp[(n,k)] = max(dp[(n,k)], find_dp(i, k-1) + tmp / (n-i))

            return dp[(n,k)]

        return find_dp(len(nums),k)


# reference: https://leetcode.com/problems/largest-sum-of-averages/discuss/122739/C%2B%2BJavaPython-Easy-Understood-Solution-with-Explanation




# greedy solution failed
""" class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # at most k subarray means k subarray in this question
        # for example b is an element in subarray B, B average is b', B' = B - b
        # there are 3 possiblities: 1. b < b', score: b + averge(B') > b + b' > b'
        #                           2. b = b', score: b + averge(B') = 2 * b' > b'
        #                           3. b > b', score: b + averge(B') > b' + averge(B') > b'
        # so k - 1 subarray cannot reach max score
        # optimal max score can be achieved when nums be split to len(nums) subarray
        # merge them to meet k subarray request
        # every time choose a minimum score loss
        # loss[i] means score loss to merge nums[i] and nums[i+1]

        loss, subarray_num = [] , len(nums)
        score = sum(nums)
        for i in range(len(nums) - 1):
            loss.append([(nums[i] + nums[i+1]) / 2, 1, i])

        while subarray_num > k:
            min_idx , min_loss = min(enumerate(loss), key = lambda x : x[1][0])
            score -= min_loss[0]
            # update loss array
            loss[min_idx][1] += 1
            loss.pop(min_idx + 1)
            pre_score_2 = sum(nums[loss[min_idx][2]:loss[min_idx][2] + loss[min_idx][1]])/loss[min_idx][1]
            if min_idx - 1 >= 0:
                pre_score_1 = sum(nums[loss[min_idx-1][2]:loss[min_idx-1][2] + loss[min_idx-1][1]])/loss[min_idx-1][1]
                new_score_1 = sum(nums[loss[min_idx-1][2]:loss[min_idx][2] + loss[min_idx][1]])/(loss[min_idx-1][1] + loss[min_idx][1])
                loss[min_idx-1][0] = pre_score_1 + pre_score_2 - new_score_1
            
            if min_idx  != len(loss)-1:
                pre_score_3 = sum(nums[loss[min_idx+1][2]:loss[min_idx+1][2] + loss[min_idx+1][1]])/loss[min_idx+1][1]
                new_score_2 = sum(nums[loss[min_idx][2]:loss[min_idx+1][2] + loss[min_idx+1][1]])/(loss[min_idx+1][1] + loss[min_idx][1])
                loss[min_idx][0] = pre_score_2 + pre_score_3 - new_score_2

          
            
            subarray_num -= 1

        return score """


        