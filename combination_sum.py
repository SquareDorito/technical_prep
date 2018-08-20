# Tags: bfs

class Solution(object):
    
    def helper(self,current,s,index):
        if s==self.target:
            self.answer.append(current)
        elif s>self.target:
            return
        for i in range(index,len(self.candidates)):
            if i>0 and self.candidates[i]==self.candidates[i-1]:
                continue
            self.helper(current+[self.candidates[i]],s+self.candidates[i],i)
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.target=target
        self.candidates=candidates
        self.candidates.sort()
        self.answer=[]
        self.helper([],0,0)
        return self.answer