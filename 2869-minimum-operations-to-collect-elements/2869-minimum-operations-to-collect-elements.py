class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        lst=[i for i in range(1,k+1)]
        result=[]
        count=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in lst and len(lst) != 0:
                lst.remove(nums[i])
                count+=1
                print(nums[i])
            elif nums[i] not in lst and len(lst) !=0:
                print(nums[i])
                count+=1
            else:
                break
        return count

