class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        frequency=[]
        prime=[2,3,5,7]
        for i in set(nums):
            if nums.count(i)>1:
                frequency.append(nums.count(i))
        prime=[]
        for i in range(2,101):
            count=0
            for j in range(2,i+1):
                if i%j==0:
                    count+=1
            if count==1 and i not in prime:
                prime.append(i)
        for i in frequency:
            if i in prime:
                return True
        return False
