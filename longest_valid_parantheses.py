# Tags: stack

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        stack.append(-1)
        ans=0
        for i,c in enumerate(s):
            if c=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans=max(ans,i-stack[-1])
        return ans