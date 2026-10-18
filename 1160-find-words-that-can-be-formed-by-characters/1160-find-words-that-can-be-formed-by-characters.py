class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        chars = list(chars)
        result=0
        for word in words:
            copy=chars.copy()
            count=0
            for i in word:
                if i in copy:
                    count+=1
                    copy.remove(i)
            if len(word)==count:
                result+=count
        return result