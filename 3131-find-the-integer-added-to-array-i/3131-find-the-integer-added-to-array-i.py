class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        result=[]
        nums1.sort()
        nums2.sort()
        n1=len(nums1)
        n2=len(nums2)
        if n1 != n2:
            return -1
        else:
            for i in range(n1):
                result.append(nums2[i]-nums1[i])
            if len(set(result))==1:
                return result[0]