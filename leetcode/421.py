import collections


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # length of max number in a binary representation
        L = len(bin(max(nums))) - 2
        max_xor = 0
        for i in range(L)[::-1]:
            # go to the next bit by the left shift
            max_xor <<= 1
            # set 1 in the smallest bit
            curr_xor = max_xor | 1
            # compute all existing prefixes 
            # of length (L - i) in binary representation
            prefixes = {num >> i for num in nums}
            # Update max_xor, if two of these prefixes could result in curr_xor.
            # Check if p1^p2 == curr_xor, i.e. p1 == curr_xor^p2
            max_xor |= any(curr_xor^p in prefixes for p in prefixes)
                    
        return max_xor


# reference：https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/solution/shu-zu-zhong-liang-ge-shu-de-zui-da-yi-huo-zhi-by-/


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        class Trie_node:
            def __init__(self) -> None:
                self.children = collections.defaultdict(Trie_node)
                self.exist = False
                self.remain = []
                self.end = False
        class Trie_tree:
            def __init__(self) -> None:
                self.root = Trie_node()
                self.res = 0
            
            def insert(self, n, s):
                cur = self.root
                for ch in s:
                    cur = cur.children[ch]
                    cur.remain.append(n)
                    cur.exist = True
                cur.end = True
                

            def search(self, n, s):
                cur = self.root
                for ch in s:
                    if ch == '0':
                        cur = cur.children['1'] if cur.children['1'].exist else cur.children['0']
                    else:
                        cur = cur.children['0'] if cur.children['0'].exist else cur.children['1']

                    if len(cur.remain) == 1 or cur.end:
                        return n ^ cur.remain[0]

        def n2s(n, L):
            l = bin(n)[2:]
            dl = L - len(l)
            return '0'* dl + l

        maxL = len(bin(max(nums))) - 2
        t = Trie_tree()
        for num in nums:
            s = n2s(num, maxL)
            t.insert(num, s)
        res = 0
        for num in nums:
            if maxL == len(bin(num)) - 2:
                res = max(res, t.search(num, n2s(num,maxL)))
        return res


