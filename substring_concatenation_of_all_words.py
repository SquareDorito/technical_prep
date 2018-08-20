# TAGS: greedy, hashmap

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        map1={}
        if not words:
            return []
        n=len(words[0])
        total_words=len(words)
        
        for w in words:
            try:
                map1[w]+=1
            except:
                map1[w]=1
                
        count=0
        ret=[]
        for i in range(n):
            map2={}
            j=i
            start=i
            count=0
            while j<=len(s)-n:
                temp=s[j:j+n]
                if temp in map1:
                    try:
                        map2[temp]+=1
                    except:
                        map2[temp]=1
                    count+=1
                    while map2[temp]>map1[temp]:
                        first=s[start:start+n]
                        map2[first]-=1
                        count-=1
                        start+=n
                    if count==total_words:
                        ret.append(start)
                        first=s[start:start+n]
                        map2[first]-=1
                        start+=n
                        count-=1
                else:
                    start=j+n
                    map2={}
                    count=0
                j+=n
        return ret