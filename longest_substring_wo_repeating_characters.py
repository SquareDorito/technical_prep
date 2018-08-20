# TAGS: hashmap, strings, greedy

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len=0
        counter=1
        wordmap={}
        prev_index=0
        
        if len(s)<=1:
            return len(s)
        
        wordmap[s[0]]=0
        for i in range(1,len(s)):
            if s[i] in wordmap:
                prev_index=wordmap[s[i]]
            else:
                prev_index=-1
            if prev_index==-1 or i-counter>prev_index:
                counter+=1
            else:
                if counter>max_len:
                    max_len=counter
                counter=i-prev_index
            wordmap[s[i]]=i
        if counter>max_len:
            return counter
        return max_len