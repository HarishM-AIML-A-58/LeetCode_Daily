from collections import Counter

class Solution(object):
    def maxOperations(self, nums, k):
        freq = Counter()
        operations = 0
        for num in nums:
            if freq[k - num] > 0:  # Pair found
                operations += 1
                freq[k - num] -= 1
            else:
                freq[num] += 1
        return operations  # Correctly indented
