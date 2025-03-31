
# 🌟 1768. Merge Strings Alternately

> 📏 **Date:** 2025-03-23  
> 🌟 **Difficulty:** `Easy`  
> 📚 **Category:** LeetCode Solutions  

---

## 📚 Problem Statement  
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

---

## 💪 Solution Approach  
🔹 **Key Concepts Used:**  
- Explain briefly what approach was used to solve the problem.

🔹 **Complexity Analysis:**  
- 🫠 **Time Complexity:** O(...)  
- 📂 **Space Complexity:** O(...)  

---

## 🖥️ Solution Code  
```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""  
        length = min(len(word1), len(word2))  
    
        for i in range(length):  
            result += word1[i] + word2[i]  

        result += word1[length:] + word2[length:]  

        return result
```

---

### 🚀 Run & Test  
```bash
python 1768._Merge_Strings_Alternately.py
```

---

### 🔗 More Solutions  
📌 [Back to main README](../../README.md)
