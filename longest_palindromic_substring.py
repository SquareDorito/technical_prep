# ========================
# Solution 1
# Tags: DP (2D table)
# ========================
class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        # create table[i][j] where s[i:j] is bool for palindrome
        table = [[False]*len(s) for _ in range(len(s))]
        start = 0
        end = 0
        for i in range(len(s)):
        	# all 1 length strings are palindromes
            table[i][i] = True
        for i in range(len(s)-1):
        	# fill table for 2 length palindromes
            if s[i] == s[i+1]:
                table[i][i+1] = True
                start = i
                end = i+1
            else:
                table[i][i+1] = False
        # build up from length 3
        for l in range(3,len(s)+1):
            for i in range(len(s)-l+1):
                j = i+l-1
                if s[i] == s[j] and table[i+1][j-1]:
                    table[i][j] = True
                    start = i
                    end = j
                else:
                    table[i][j] = False
        return s[start:end+1]

# ===================================
# Solution 2
# Tags: Greedy (expand around center)
# ===================================

class Solution:
    def expand_around_center(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1
    
    def longestPalindrome(self, s):
        if not s:
            return ""
        if len(s) == 1:
            return s
        start,end=0,0
        for i in range(len(s)):
            len1=self.expand_around_center(s,i,i)
            len2=self.expand_around_center(s,i,i+1)
            temp_len=len1 if len1>len2 else len2
            if temp_len>end-start:
                print(i,temp_len)
                start=i-(temp_len-1)//2
                end=i+(temp_len//2)
        return s[start:end+1]