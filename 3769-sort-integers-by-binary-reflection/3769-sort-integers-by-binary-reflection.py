class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        binary=[]
        for i in nums:
            conversion=(bin(i)[2:])[::-1]
            b=int(conversion,2)
            binary.append(b)
        result=[i for i in zip(binary,nums)]
        result=sorted(result)
        binary,nums=zip(*result)
        return nums