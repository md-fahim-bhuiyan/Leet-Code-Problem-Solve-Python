from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            lo, hi = i + 1, n - 1
            while lo < hi:
                current = nums[i] + nums[lo] + nums[hi]
                if current == target:
                    return target
                if abs(current - target) < abs(closest - target):
                    closest = current
                if current < target:
                    lo += 1
                else:
                    hi -= 1
        return closest
