
        # 🌟 1679. Max Number of K-Sum Pairs

> 🗓 **Date:** 2025-04-03  
> 🎯 **Difficulty:** `Medium`  
> 📂 **Category:** LeetCode Solutions  

---

## 📖 Problem Statement  
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

---

## 💡 Solution Approach  
🔹 **Key Concepts Used:**  
- Explain briefly what approach was used to solve the problem.

🔹 **Complexity Analysis:**  
- 🕑 **Time Complexity:** O(...)  
- 💾 **Space Complexity:** O(...)  

---

## 🖥️ Solution Code  
```python
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

```

---

### 🚀 **Run & Test**  
```bash
python 1679_Max_Number_of_K-Sum_Pairs.py
```

---

### 🔗 **More Solutions**  
📌 [Back to main README](../../README.md)
