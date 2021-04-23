class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for i in range(0,len(magazine)):
            if mag_dict.get(magazine[i]) == None:
                mag_dict[magazine[i]] = 1
            else:
                mag_dict[magazine[i]] += 1

        for i in range(0,len(ransomNote)):
            if mag_dict.get(ransomNote[i]) == None:
                return False
            else:
                mag_dict[ransomNote[i]] -= 1
                if mag_dict[ransomNote[i]] < 0:
                    return False
            
        return True
                