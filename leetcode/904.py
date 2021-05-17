class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        type_rcd = []
        bpt = 0 
        cnt , ans = 0 , 0 
        for i in range(len(tree)):
            if tree[i] in type_rcd:
                cnt += 1
                if tree[i] != tree[i - 1]:
                    bpt = i
            else:
                if len(type_rcd) < 2:
                    type_rcd.append(tree[i])
                    bpt = i
                    cnt += 1
                else:
                    type_rcd.remove(tree[bpt - 1])
                    cnt = i - bpt + 1
                    bpt = i
                    type_rcd.append(tree[i])
            ans = cnt if cnt > ans else ans

        return ans
        
                    
