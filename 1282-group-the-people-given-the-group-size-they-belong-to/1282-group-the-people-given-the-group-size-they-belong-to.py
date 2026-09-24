class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        result=[]
        for i in set(groupSizes):
            lst=[]
            for j in range(len(groupSizes)):
                if  i==groupSizes[j]:
                    lst.append(j)
                    if len(lst)==i:
                        result.append(lst)
                        lst=[]
        return result
