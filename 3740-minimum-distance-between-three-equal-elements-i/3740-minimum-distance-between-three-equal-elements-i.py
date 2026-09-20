class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]==nums[j]==nums[k]:
                        total=abs(i-j)+abs(j-k)+abs(k-i)
                        result.append(total)
        if len(result) != 0:
            return min(result)
        else:
            return -1
