class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=(int("".join(map(str,digits))))+1
        r=list(map(int,str(result)))
        return r