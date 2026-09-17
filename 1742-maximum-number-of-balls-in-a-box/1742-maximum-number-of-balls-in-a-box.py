class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        result=[]
        for i in range(lowLimit,highLimit+1):
            digit_sum=0
            while i>0:
                rev=i%10
                digit_sum=digit_sum+rev
                i=i//10
            result.append(digit_sum)
        dicts={}
        for i in result:
            if i in dicts:
                dicts[i]+=1
            else:
                dicts[i]=1
        max_count=0
        for key,value in dicts.items():
            if value>max_count:
                max_count=value
        return max_count
        
