class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for i in s:
            if i=='(' or i=="[" or i=="{":
                arr.append(i)
            else:
                if len(arr) ==0:
                    return False
                top=arr.pop()
                if i==')' and top != '(':
                    return False
                elif i== ']' and top !='[':
                    return False
                elif i=='}' and top !='{':
                    return False
        return len(arr)==0