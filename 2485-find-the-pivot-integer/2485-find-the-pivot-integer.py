class Solution:
    def pivotInteger(self, n: int) -> int:
        lst=[i for i in range(1,n+1)]
        total=sum(lst)
        left=0
        right=0
        for i in range(len(lst)):
            right=total-left-lst[i]
            if left==right:
                return lst[i]
            left+=lst[i]
        else:
            return -1