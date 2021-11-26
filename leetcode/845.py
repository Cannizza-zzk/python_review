class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        forward_list = [0]
        backward_list = [0]
        res = []

        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                forward_list.append(forward_list[i-1] + 1)
            else:
                forward_list.append(0)
        for i in range(len(arr)-2,-1,-1):
            if arr[i] > arr[i+1]:
                backward_list.append(backward_list[-1]+1)
            else:
                backward_list.append(0)

        backward_list.reverse()
        for i in range(len(arr)):
            if forward_list[i] != 0 and backward_list[i] != 0:
                res.append(forward_list[i] + backward_list[i])
            else:
                res.append(0)
        #print(backward_list)
        #print(forward_list)
        return max(res) + 1 if max(res) + 1 >= 3 else 0




# dp solution time limited
""" class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # dp[i][j] == 1 means arr[i:j+1] is a mountain
        # dp[i][j] = (dp[i+1][j-1] and arr[i] < arr[i+1] and arr[j] < arr[j-1])
        #          or (dp[i+1][j] and arr[i] < arr[i+1])
        #          or (dp[i][j-1] and arr[j] < arr[j-1])

        res = 0
        dp = [[0 for _ in range(len(arr))] for _  in range(len(arr))]
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] < arr[i + 1] and arr[i+2] < arr[i+1]:
                dp[i][i+2] = 1
                res = 3

                for j in range(i + 3, len(arr)):
                    dp[i][j] = (dp[i+1][j-1] and arr[i] < arr[i+1] and arr[j] < arr[j-1])\
                    or (dp[i+1][j] and arr[i] < arr[i+1])\
                    or (dp[i][j-1] and arr[j] < arr[j-1])

                    res = max(res,(j-i)+1) if dp[i][j] == 1 else res
                

        return res """

        
