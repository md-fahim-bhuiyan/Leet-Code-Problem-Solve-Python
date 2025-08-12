class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empties.append((r, c))
                else:
                    num = int(board[r][c])
                    mask = 1 << num
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + (c // 3)] |= mask

        def backtrack(i):
            if i == len(empties):
                return True
            r, c = empties[i]
            b = (r // 3) * 3 + (c // 3)
            for num in range(1, 10):
                mask = 1 << num
                if not (rows[r] & mask or cols[c] & mask or boxes[b] & mask):
                    board[r][c] = str(num)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[b] |= mask
                    if backtrack(i + 1):
                        return True
                    board[r][c] = "."
                    rows[r] &= ~mask
                    cols[c] &= ~mask
                    boxes[b] &= ~mask
            return False

        backtrack(0)
