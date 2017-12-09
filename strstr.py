class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == "":
            if needle == "":
                return 0
            else:
                return -1
        
        if needle == "":
            return 0
        
        srclen = len(haystack)
        needlelen = len(needle)
        
        if needlelen > srclen:
            return -1
        
        pos = -1
        
        for start in range(0, srclen):
            i = start
            j = 0
            
            if srclen - start < needlelen:
                break
            
            while needlelen > j and srclen > i and haystack[i] == needle[j]:
                i = i + 1
                j = j + 1
            
            if j == needlelen:
                pos = start
                break
        
        
        return pos