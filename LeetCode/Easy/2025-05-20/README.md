
        # 🌟 125. Valid Palindrome

> 🗓 **Date:** 2025-05-20  
> 🎯 **Difficulty:** `Easy`  
> 📂 **Category:** LeetCode Solutions  

---

## 📖 Problem Statement  
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

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
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1

        while left < right:
           
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

```

---

### 🚀 **Run & Test**  
```bash
python 125_Valid_Palindrome.py
```

---

### 🔗 **More Solutions**  
📌 [Back to main README](../../README.md)
