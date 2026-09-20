class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        result=[]
        for i in range(len(bulbs)):
            if bulbs[i] not in result:
                result.append(bulbs[i])
            else:
                result.remove(bulbs[i])
        result.sort()
        return result