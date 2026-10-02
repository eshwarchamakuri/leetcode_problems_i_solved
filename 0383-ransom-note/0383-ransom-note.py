class Solution:
    def canConstruct(self, s: str, t: str) -> bool:
        arr1=[0]*26
        arr2=[0]*26
        for i in s:
            index=(ord(i)-ord('a'))
            arr1[index]+=1
        for i in t:
            index1=(ord(i)-ord('a'))
            arr2[index1]+=1
        for i in range(26):
            if arr1[i]>arr2[i]:
                return False
        return True

      
