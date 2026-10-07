class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        result=[]
        for i in range(len(nums)):
            count=0
            for j in range(i+1,len(nums)):
                if nums[i]%2==0:
                    if nums[j]%2!=0:
                        count+=1
                else:
                    if nums[j]%2==0:
                        count+=1
            result.append(count)
        return result

                