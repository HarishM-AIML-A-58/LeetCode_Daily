
# 🌟 1071. Greatest Common Divisor of Strings

> 📏 **Date:** 2025-03-24  
> 🌟 **Difficulty:** `Easy`  
> 📚 **Category:** LeetCode Solutions  

---

## 📚 Problem Statement  
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

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
import fractions
class Solution(object):

    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        
        max_length = fractions.gcd(len(str1), len(str2))
        candidate = str1[:max_length]
        return candidate
```

---

### 🚀 Run & Test  
```bash
python 1071._Greatest_Common_Divisor_of_Strings.py
```

---

### 🔗 More Solutions  
📌 [Back to main README](../../../README.md)
