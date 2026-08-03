class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def getidxs(boxidx, cellidx):
            col = (cellidx % 3) + 3*(boxidx % 3)
            row = (cellidx // 3) + 3*(boxidx // 3)
            return col,row
        for i in range(9):
            boxmap = set()
            colmap = set()
            rowmap = set()
            for j in range(9):
                hcell = board[i][j]
                vcell = board[j][i]

                if hcell in rowmap:
                    return False
                elif hcell != ".":
                    rowmap.add(hcell)
                if vcell in colmap:
                    return False
                elif vcell != ".":
                    colmap.add(vcell)

                col,row = getidxs(i,j)
                bcell = board[col][row]
                if bcell in boxmap:
                    return False
                elif bcell != ".":
                    boxmap.add(bcell)
        return True