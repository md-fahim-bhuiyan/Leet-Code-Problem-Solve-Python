class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        combo = []

        def backtrack(start):
            if len(combo) == k:
                res.append(combo[:])
                return
            for i in range(start, n + 1):
                combo.append(i)
                backtrack(i + 1)
                combo.pop()

        backtrack(1)
        return res
