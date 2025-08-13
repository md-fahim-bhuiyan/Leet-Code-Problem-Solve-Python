class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        word_len = len(word)

        def backtrack(r, c, index):
            if index == word_len:
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            found = (
                backtrack(r + 1, c, index + 1) or
                backtrack(r - 1, c, index + 1) or
                backtrack(r, c + 1, index + 1) or
                backtrack(r, c - 1, index + 1)
            )

            board[r][c] = temp
            return found

        from collections import Counter
        board_counter = Counter(c for row in board for c in row)
        word_counter = Counter(word)
        for ch in word_counter:
            if word_counter[ch] > board_counter.get(ch, 0):
                return False

        if board_counter[word[0]] > board_counter[word[-1]]:
            word = word[::-1]

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True

        return False