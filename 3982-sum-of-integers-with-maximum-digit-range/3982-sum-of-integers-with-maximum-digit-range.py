class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        total=[]
        for i in nums:
            i=str(i)
            lst=[int(digit) for digit in str(i)]
            mx=max(lst)
            mm=min(lst)
            t1=mx-mm
            total.append(t1)
            max1=max(total)
        result=0
        for i in range(len(total)):
            if total[i]==max1:
                result+=nums[i]
        return result