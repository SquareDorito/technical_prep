# Tags: greedy

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        c1,c2=0,len(matrix[0])-1
        r1,r2=0,len(matrix)-1
        answer=[]
        while True:
            for i in range(c1,c2+1):
                answer.append(matrix[r1][i])
            r1+=1
            if r1>r2:
                break
            
            for i in range(r1,r2+1):
                answer.append(matrix[i][c2])
            c2-=1
            if c1>c2:
                break
            
            for i in reversed(range(c1,c2+1)):
                answer.append(matrix[r2][i])
            r2-=1
            if r1>r2:
                break
            
            for i in reversed(range(r1,r2+1)):
                answer.append(matrix[i][c1])
            c1+=1
            if c1>c2:
                break
                
        return answer