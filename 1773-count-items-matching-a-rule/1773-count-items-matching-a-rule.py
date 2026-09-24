class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        if ruleKey=='type':
            ruleKey=0
        elif ruleKey=='color':
            ruleKey=1
        else:
            ruleKey=2
        for item in items:
            if item[ruleKey]==ruleValue:
                count+=1
        return count
                