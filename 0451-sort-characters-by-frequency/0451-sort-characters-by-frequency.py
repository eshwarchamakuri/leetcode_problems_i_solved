class Solution:
    def frequencySort(self, s: str) -> str:
        dicts={}
        for i in s:
            if i in dicts:
                dicts[i]+=1
            else:
                dicts[i]=1
        dicts=dict(sorted(dicts.items(),key = lambda x:x[1],reverse=True))
        result=""
        for key,value in dicts.items():
            result+=key*value
        return result