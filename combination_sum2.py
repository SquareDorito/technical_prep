# Tags: bfs

class Solution(object):
    
    def helper(self,nums,current,s,index):
        if s==self.target:
            self.answer.append(current)
        elif s>self.target:
            return
        i=index
        while i<len(nums):
            self.helper(nums,current+[nums[i]],s+nums[i],i+1)
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            i+=1
            
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.target=target
        self.answer=[]
        self.helper(sorted(candidates),[],0,0)
        return self.answer