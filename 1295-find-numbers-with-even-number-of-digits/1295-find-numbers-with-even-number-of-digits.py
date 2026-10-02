class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        result=list(map(str,nums))
        for i in result:
            if len(i)%2==0:
                count+=1
        return count