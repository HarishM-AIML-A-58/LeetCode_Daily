import fractions
class Solution(object):

    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        
        max_length = fractions.gcd(len(str1), len(str2))
        candidate = str1[:max_length]
        return candidate