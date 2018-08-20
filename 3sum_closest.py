# TAGS: Greedy
# Notes: Came up on Alation technical.

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        best=float('inf')
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            left_sum=nums[i]+nums[l]+nums[l+1]
            right_sum=nums[i]+nums[r]+nums[r-1]
            if left_sum>target:
                if left_sum-target<abs(best):
                    best=left_sum-target
            elif right_sum<target:
                if target-right_sum<abs(best):
                    best=right_sum-target
            else:
                while l<r:
                    temp=nums[i]+nums[l]+nums[r]
                    if temp>target:
                        r-=1
                        if temp-target<abs(best):
                            best=temp-target
                    elif temp<target:
                        l+=1
                        if target-temp<abs(best):
                            best=temp-target
                    else:
                        return target
        return target+best