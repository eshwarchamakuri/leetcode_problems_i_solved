class Solution:
    def findMin(self, nums: list[int]) -> int:
        i=0
        j=len(nums)-1
        while i<j:
            mid=(i+j)//2
            if nums[i]==nums[mid]==nums[j]:
                i+=1
                j-=1
            elif nums[mid]<=nums[j]:
                j=mid
            else:
                i=mid+1
        return nums[i]