class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        compare=[i+1 for i in range(len(matrix))]
        result=True
        for i in range(len(matrix)):
            column=[]
            row=[]
            for j in range(len(matrix[0])):
                column.append(matrix[j][i])
            for k in range(len(matrix[0])):
                row.append(matrix[i][k])
            column.sort()
            row.sort()
            if column != compare or row != compare:
                result=False
                break
        return result
