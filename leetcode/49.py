class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
        anagrams = collections.defaultdict(list)
        for word in strs:
            cnt =  collections.Counter(word)
            encode = ''
            for i in range(ord('a'), ord('z') + 1):
                encode += chr(i) + str(cnt[chr(i)])
            #print(encode)
            anagrams[encode].append(word)
        res = []
        for _, v in anagrams.items():
            res.append(v)

        return res

# C++ solution:https://leetcode.com/problems/group-anagrams/discuss/19200/C%2B%2B-unordered_map-and-counting-sort