class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        dense_count = []
        total_num , sample_sum = 0, 0
        mode, mode_cnt = 0 , 0
        for integer , cnt in enumerate(count):
            if cnt != 0:
                dense_count.append([integer,cnt])
                total_num += cnt
                sample_sum += cnt * integer
                if cnt > mode_cnt:
                    mode_cnt = cnt
                    mode = float(integer)

        minimum, maximum, mean, median = 0, 0, 0, 0
        minimum = float(dense_count[0][0])
        maximum = float(dense_count[-1][0])
        mean = float(sample_sum/total_num)
        median_index = total_num // 2 + 1 if total_num % 2 == 1 else total_num//2
        cnt = 0
        for index ,int_pair in enumerate(dense_count):
            cnt += int_pair[1]
            if median_index <= cnt:
                if total_num % 2 == 1:
                    median = float(int_pair[0])
                else:
                    if median_index == cnt:
                        median = float((int_pair[0] + dense_count[index+1][0]) / 2)
                    else:
                        median = float(int_pair[0])
                break
        return [minimum,maximum,mean,median,mode]
        
