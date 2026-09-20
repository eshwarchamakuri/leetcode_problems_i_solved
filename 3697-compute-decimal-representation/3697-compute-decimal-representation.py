class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        string=list(str(n))[::-1]
        result=[]
        k=1
        for i in string:
            total=int(i)*k
            if total !=0:
                result.append(total)
            k*=10
        return result[::-1]
        
