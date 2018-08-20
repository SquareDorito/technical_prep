# TAGS: greedy

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start=0
        end=len(height)-1
        max_volume=0
        while start<end:
            if height[start]>height[end]:
                temp_vol=(end-start)*height[end]
                if temp_vol>max_volume:
                    max_volume=temp_vol
                end-=1
            else:
                temp_vol=(end-start)*height[start]
                if temp_vol>max_volume:
                    max_volume=temp_vol
                start+=1
        return max_volume