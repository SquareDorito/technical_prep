# TAGS: greedy, hashmap

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        d={'(':')','[':']','{':'}'}
        for i in range(len(s)):
            if s[i]=='{' or s[i]=='(' or s[i]=='[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if s[i]!=d[stack.pop()]:
                    return False
        if stack:
            return False
        return True