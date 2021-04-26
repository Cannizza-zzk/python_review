class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleID = -1
        if ruleKey == 'type':
            ruleID = 0 
        elif ruleKey == 'color':
            ruleID = 1
        else:
            ruleID = 2
        cnt = 0
        for i in range(0,len(items)):
            if items[i][ruleID] == ruleValue:
                cnt += 1
        
        return cnt