class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        lst1=[]
        lst2=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                lst1.append(nums[i])
            else:
                lst2.append(nums[i])
        result=[]
        k1=0
        k2=0
        for i in range(len(nums)):
            if i%2==0:
                result.append(lst1[k1])
                k1+=1
            else:
                result.append(lst2[k2])
                k2+=1
        return result
