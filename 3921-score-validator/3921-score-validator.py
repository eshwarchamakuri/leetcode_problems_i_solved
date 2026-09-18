class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score=0
        counter=0
        for i in events:
            if i.isdigit():
                score+=int(i)
            else:
                if i=="WD":
                    score+=1
                elif i=="NB":
                    score+=1
                else:
                    counter+=1
                    if counter==10:
                        return [score,counter]
        return [score,counter]
