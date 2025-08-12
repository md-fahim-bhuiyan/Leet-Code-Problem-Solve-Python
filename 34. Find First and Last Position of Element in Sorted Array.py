class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(bias):
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target: l = m + 1
                elif nums[m] > target: r = m - 1
                else:
                    res = m
                    if bias == 'left': r = m - 1
                    else: l = m + 1
            return res
        return [find('left'), find('right')]
