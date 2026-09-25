class Solution:
    def minElement(self, nums: List[int]) -> int:
        result=[]
        for i in nums:
            total=0
            s=str(i)
            for i in s:
                total+=int(i)
            result.append(total)
        return min(result)