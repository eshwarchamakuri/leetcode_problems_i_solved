class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        max_count=s.count('(')+s.count(')')
        valid_pass=0
        stack=[]
        for i in s:
            if i=='(':
                stack.append(i)
            else:
                if len(stack)>0:
                    stack.pop()
                    valid_pass+=2
                
        return max_count-valid_pass
            