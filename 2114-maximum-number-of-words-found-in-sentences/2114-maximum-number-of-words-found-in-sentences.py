class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        length=0
        for sentence in sentences:
            sentence=sentence.split()
            if len(sentence)>length:
                length=len(sentence)
        return length
        