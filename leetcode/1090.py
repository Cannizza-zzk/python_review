class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        label_rcd = {}
        vlList =[]
        ans = []
        for label in labels:
            if label not in label_rcd:
                label_rcd[label] = 0
        for i in range(len(values)):
            vlList.append((values[i],labels[i]))
        vlList.sort(key= lambda x : x[0],reverse = True)
        #print(vlList)
        i = 0
        while len(ans) < num_wanted and i < len(vlList):
            if label_rcd[vlList[i][1]] < use_limit:
                label_rcd[vlList[i][1]] += 1
                ans.append(vlList[i][0])
            i += 1

        return sum(ans)


