class Solution(object):
    def findTheDifference(self, s, t):
        return list((Counter(t) - Counter(s)).elements())[0]

        