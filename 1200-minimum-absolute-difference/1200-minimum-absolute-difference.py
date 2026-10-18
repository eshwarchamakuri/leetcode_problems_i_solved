class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        difference=float('inf')
        for i in range(len(arr)-1):
            min_diff=arr[i+1]-arr[i]
            if min_diff<difference:
                difference=min_diff
        result=[]
        for i in range(len(arr)-1):
            if (arr[i+1]-arr[i])==difference:
                result.append([arr[i],arr[i+1]])
        return result
        