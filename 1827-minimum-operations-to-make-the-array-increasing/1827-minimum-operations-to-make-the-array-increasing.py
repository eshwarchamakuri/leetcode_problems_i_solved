class Solution:
    def minOperations(self, arr: List[int]) -> int:
        result=[]
        count=0
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                result.append(arr[i])
            else:
                modify=arr[i]-arr[i+1]+1
                element=arr[i+1]+modify
                arr.remove(arr[i+1])
                arr.insert(i+1,element)
                count+=modify
        return count