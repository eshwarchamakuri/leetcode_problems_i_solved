class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(matrix[mat]) for mat in range(len(matrix))]