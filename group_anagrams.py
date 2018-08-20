# =================================
# Solution 1
# Tags: sorted strings comparison
# =================================

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for s in strs:
            temp=''.join(sorted(s))
            try:
                d[temp].append(s)
            except:
                d[temp]=[s]
        ret=[]
        for key in d:
            ret.append(d[key])
        return ret
        
# =================================
# Solution 2
# Tags: num chars comparison (hash)
# =================================