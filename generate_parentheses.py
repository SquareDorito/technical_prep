# =========================
# Solution 1
# Tags: Recursive
# =========================

class Solution(object):
    
    def helper(self,curr, pos, num_open, num_close):
        if(num_close == self.n):
            self.results.append(''.join(curr))
            return
        else:
            if(num_open > num_close):
                curr[pos] = ')';
                self.helper(curr, pos + 1, num_open, num_close + 1);
            if(num_open < self.n):
                curr[pos] = '(';
                self.helper(curr, pos + 1, num_open + 1, num_close);
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==1:
            return ['()']
        self.n=n
        self.results=[]
        temp=['' for i in range(2*n)]
        self.helper(temp,0,0,0)
        return self.results


# =========================
# Solution 2
# Tags: DP
# =========================

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]