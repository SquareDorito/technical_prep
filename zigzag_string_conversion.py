# TAGS: strings

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if len(s)<=1 or numRows==1:
            return s
        
        increment=2*numRows-2
        answer=""
        
        for row in range(numRows):
            i=2*(numRows-row-1)
            j=increment-i
            temp_index=row
            if j==0 or i==0:
                while temp_index<len(s):
                    answer+=s[temp_index]
                    temp_index+=increment  
            else:
                tempbool=True
                while temp_index<len(s):
                    answer+=s[temp_index]
                    if tempbool:
                        temp_index+=i
                    else:
                        temp_index+=j
                    tempbool= not tempbool
        return answer