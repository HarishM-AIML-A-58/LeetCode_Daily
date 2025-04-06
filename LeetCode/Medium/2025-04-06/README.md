
        # 🌟 1456. Maximum Number of Vowels in a Substring of Given Length

> 🗓 **Date:** 2025-04-06  
> 🎯 **Difficulty:** `Medium`  
> 📂 **Category:** LeetCode Solutions  

---

## 📖 Problem Statement  
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2

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
    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        max_count = 0
        
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            max_count = max(max_count, count)
        
        return max_count
```

---

### 🚀 **Run & Test**  
```bash
python 1456_Maximum_Number_of_Vowels_in_a_Substring_of_Given_Length.py
```

---

### 🔗 **More Solutions**  
📌 [Back to main README](../../README.md)
