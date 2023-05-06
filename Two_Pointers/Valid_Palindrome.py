class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.upper()
        s1 = ""
        s2 = ""
        for x in s:
            if(x.isalnum()):
                s1=s1+x
                s2 = x+s2
        return s1==s2
