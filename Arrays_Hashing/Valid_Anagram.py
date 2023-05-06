class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lst=[0]*45
        ctr=0
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            lst[ord(s[i])-ord('a')]+=1
            lst[ord(t[i])-ord('a')]-=1
        for x in range(45):
            if(lst[x]==0):
                ctr = ctr+1
        return ctr==45


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        q="".join(sorted(s))
        p="".join(sorted(t))
        return q==p
