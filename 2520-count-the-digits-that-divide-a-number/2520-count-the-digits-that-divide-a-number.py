class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        real=num
        while num !=0:
            rev=num%10
            if real%rev==0:
                count+=1
            num//=10
        return count