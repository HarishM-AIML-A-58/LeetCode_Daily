class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a=list()
        for i in range(len(candies)):
            if (candies[i]+extraCandies>=max(candies)):
                a.append(True)
            else:
                a.append(False)
        return a