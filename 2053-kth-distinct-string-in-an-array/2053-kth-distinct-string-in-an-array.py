class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        string=[]
        for i in range(len(arr)):
            if arr.count(arr[i])==1 and arr[i] not in string:
                string.append(arr[i])
        print(string)
        if len(string)>=k:
            result=""
            for i in range(k):
                result=string[i]
            return result
        else:
            return ""