class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        lst=[]
        s=""
        for i in word:
            if i.isdigit():
                s+=i
            else:
                print(s)
                if s !="":
                    if int(s) not in lst:
                        lst.append(int(s))
                    s=""
        if s !="":
            if int(s) not in lst:
                lst.append(int(s))
        
        return len(lst)
        


                