class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        l=len(nums[0])
        s='1'*l
        n=int(s,2)
        for i in range(n+1):
            result=bin(i)[2:].zfill(len(s))
            if result not in nums:
                return result
                break
        