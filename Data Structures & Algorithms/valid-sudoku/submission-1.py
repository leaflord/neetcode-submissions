class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            boxmap = set()
            colmap = set()
            rowmap = set()
            for j in range(9):
                hcell = board[i][j]
                vcell = board[j][i]
                bcell = board[(j % 3) + 3 * (i % 3)][(j // 3) + 3 * (i // 3)]
                if hcell in rowmap or vcell in colmap or bcell in boxmap:
                    return False
                if hcell != ".":
                    rowmap.add(hcell)
                if vcell != ".":
                    colmap.add(vcell)
                if bcell != ".":
                    boxmap.add(bcell)
        return True