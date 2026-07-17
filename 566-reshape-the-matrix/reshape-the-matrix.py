class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat
        
        arr = []
        for i in mat:
            arr = arr + i

        ans = []
        for i in range(r):
            ans.append(arr[:c])
            arr = arr[c:]
        return ans

        