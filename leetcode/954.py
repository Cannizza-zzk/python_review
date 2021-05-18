class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key = abs)
        usable_rcd = Counter(arr)
        for elem in arr:
            if usable_rcd[elem] > 0 :
                usable_rcd[elem] -= 1 
                if elem * 2 in usable_rcd and usable_rcd[elem * 2] > 0:
                    usable_rcd[elem * 2] -= 1
                else:
                    return False
             
        return True

# python 中使用in查找某个元素，字典查找的速度>>列表查找的速度
# list的存储形式是线性表，查找的效率其实是O(n)；dict的存储形式是哈希表，查找的效率是O(1)
# 二者执行效率上相差了近10000倍
# reference: https://blog.csdn.net/jmh1996/article/details/78481365
        