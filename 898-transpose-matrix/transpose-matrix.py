class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        ROW = len(matrix)
        COL = len(matrix[0])
        for col in range(COL):
            new_res = []
            for row in range(ROW):
                new_res.append(matrix[row][col])
            res.append(new_res)
        return res


        