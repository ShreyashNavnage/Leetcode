class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    r_key = (i, val)
                    c_key = (val, j)
                    b_key = (i // 3, j // 3, val)
                    if r_key in seen or c_key in seen or b_key in seen:
                        return False
                    seen.add(r_key)
                    seen.add(c_key)
                    seen.add(b_key)
        return True