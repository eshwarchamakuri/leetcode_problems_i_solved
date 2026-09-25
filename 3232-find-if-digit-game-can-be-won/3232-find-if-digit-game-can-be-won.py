class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single=0
        doudle=0
        for i in nums:
            s=str(i)
            if len(s)==2:
                doudle+=i
            else:
                single+=i
        if doudle==single:
            return False
        else:
            return True