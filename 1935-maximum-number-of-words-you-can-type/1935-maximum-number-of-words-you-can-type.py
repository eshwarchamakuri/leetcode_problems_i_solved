class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split()
        total_length=len(text)
        count=0
        for i in range(total_length):
            for j in text[i]:
                if j in brokenLetters:
                    count+=1
                    break
        return total_length-count