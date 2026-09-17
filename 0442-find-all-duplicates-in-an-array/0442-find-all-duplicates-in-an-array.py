class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        lst=[0]*100001
        for i in nums:
            lst[i]+=1
        result=[]
        for i in range(len(lst)):
            if lst[i]==2:
                result.append(i)
        return result

        