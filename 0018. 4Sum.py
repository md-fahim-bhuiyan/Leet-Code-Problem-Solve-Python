from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums); r=[]
        for i in range(n-3):
            if i and nums[i]==nums[i-1]: continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]: continue
                l,h=j+1,n-1
                while l<h:
                    s=nums[i]+nums[j]+nums[l]+nums[h]
                    if s==target:
                        r.append([nums[i],nums[j],nums[l],nums[h]])
                        l+=1; h-=1
                        while l<h and nums[l]==nums[l-1]: l+=1
                        while l<h and nums[h]==nums[h+1]: h-=1
                    elif s<target: l+=1
                    else: h-=1
        return r
