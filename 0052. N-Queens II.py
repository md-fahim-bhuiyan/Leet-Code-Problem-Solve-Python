class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        cols = set()
        pos_diags = set()  
        neg_diags = set() 

        def backtrack(r):
            nonlocal count
            if r == n:
                count += 1
                return
            for c in range(n):
                if c in cols or (r + c) in pos_diags or (r - c) in neg_diags:
                    continue
                cols.add(c)
                pos_diags.add(r + c)
                neg_diags.add(r - c)

                backtrack(r + 1)

                cols.remove(c)
                pos_diags.remove(r + c)
                neg_diags.remove(r - c)

        backtrack(0)
        return count
