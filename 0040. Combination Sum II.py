from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        comb = []
        def backtrack(start, remaining):
            if remaining == 0:
                res.append(comb.copy())
                return
            if remaining < 0:
                return
            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                if candidates[i] > remaining:
                    break
                comb.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                comb.pop()
                prev = candidates[i]
        backtrack(0, target)
        return res
