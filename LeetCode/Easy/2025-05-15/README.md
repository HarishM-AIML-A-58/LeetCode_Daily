
        # 🌟 2215. Find the Difference of Two Arrays

> 🗓 **Date:** 2025-05-15  
> 🎯 **Difficulty:** `Easy`  
> 📂 **Category:** LeetCode Solutions  

---

## 📖 Problem Statement  
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

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
class Solution(object):
    def findDifference(self, nums1, nums2):

        set1 = set(nums1)
        set2 = set(nums2)
        
        diff1 = list(set1 - set2)
        diff2 = list(set2 - set1)
        
        return [diff1, diff2]
```

---

### 🚀 **Run & Test**  
```bash
python 2215_Find_the_Difference_of_Two_Arrays.py
```

---

### 🔗 **More Solutions**  
📌 [Back to main README](../../README.md)
