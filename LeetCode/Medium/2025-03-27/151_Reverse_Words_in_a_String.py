class Solution(object):
    def reverseWords(self, s):
        a=s.split()
        a.reverse()
        b=" ".join(a)
        return b