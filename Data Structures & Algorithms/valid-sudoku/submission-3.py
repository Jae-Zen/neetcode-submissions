class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                elif ( num in rows.get(r, set())
                    or num in cols.get(c, set())
                    or num in squares.get((r // 3, c // 3), set())):
                    return False
                else:
                    if not rows.get(r):
                        rows[r] = set()
                    if not cols.get(c):
                        cols[c] = set()
                    if not squares.get((r // 3, c // 3)):
                        squares[(r // 3, c // 3)] = set()
                    rows[r].add(num)
                    cols[c].add(num)
                    squares[(r // 3, c // 3)].add(num)
        return True



        