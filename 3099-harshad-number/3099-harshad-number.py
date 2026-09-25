class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=list(str(x))
        result=0
        for i in s:
            result+=int(i)
        if x%result==0:
            return result
        else:
            return -1
