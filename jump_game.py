# Tags: dp?

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_dist=0
        if len(nums)==1:
            return True
        for i in range(len(nums)):
            if max_dist<=i and nums[i]==0:
                return False
            max_dist=max(max_dist,i+nums[i])

            if max_dist>=len(nums)-1:
                return True
        return False